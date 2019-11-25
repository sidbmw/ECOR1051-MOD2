from Cimpl import create_color, create_image, get_color, set_color, Image
from L5_6_P4_extreme import extreme_contrast
from L5_6_P4_sepia import sepia
from L5_6_P4_three_tone import three_tone
from L5_6_P4_two_tone import two_tone as tt
from L5_6_P5_edge import detect_edges
from L5_6_P5_imp_edge import detect_edges_better
from test_grayscale import check_equal


def check_equal(description: str, outcome, expected) -> None:
    """
    Author: Prof. Donald L. Bailey
    Print a "passed" message if outcome and expected have same type and
    are equal (as determined by the == operator); otherwise, print a
    "fail" message.

    Parameter description should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    outcome.

    Parameters outcome and expected are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal.
    """
    outcome_type = type(outcome)
    expected_type = type(expected)
    if outcome_type != expected_type:

        # The format method is explained on pages 119-122 of
        # 'Practical Programming', 3rd ed.

        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but outcome ({3}) has type {4}".
              format(description, expected,
                     str(expected_type).strip('<class> '),
                     outcome, str(outcome_type).strip('<class> ')))
    elif outcome != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, outcome))
    else:
        print("{0} PASSED".format(description))
    print("------")


def test_detect_edge() -> None:
    """Returns whether the edge detection filter works and if it didn't,\
    indicates where it wasn't applied.
    -Test function written by Leanne Matamoros - 10114740

    >>> test_edge()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(4, 1) PASSED
    ------

    >>> test_edge()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) FAILED: expected Color(red=255, green=255,\
    blue=255), got Color(red=0, green=0, blue=0)
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(1, 1) PASSED
    ------
    Checking pixel @(2, 1) PASSED
    ------
    Checking pixel @(3, 1) PASSED
    ------
    Checking pixel @(4, 1) PASSED
    ------
    """
    original = create_image(5, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 10, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))

    set_color(original, 0, 1, create_color(10, 30, 3))
    set_color(original, 1, 1, create_color(67, 90, 1))
    set_color(original, 2, 1, create_color(0, 2, 20))
    set_color(original, 3, 1, create_color(189, 53, 222))
    set_color(original, 4, 1, create_color(145, 136, 198))

    expected = create_image(5, 2)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(255, 255, 255))
    set_color(expected, 4, 0, create_color(0, 0, 0))

    # The last row's value stay the same do to the criterias of the edge
    # detection filter.

    set_color(expected, 0, 1, create_color(10, 30, 3))
    set_color(expected, 1, 1, create_color(67, 90, 1))
    set_color(expected, 2, 1, create_color(0, 2, 20))
    set_color(expected, 3, 1, create_color(189, 53, 222))
    set_color(expected, 4, 1, create_color(145, 136, 198))

    # threshold is assigned 15 for this test

    image_edge = detect_edges(original, 15)

    for x, y, col in image_edge:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_extreme() -> None:
    """A test function for extreme contrast.
    -Test function written by Leanne Matamoros - 101147405

    >>> test_extreme()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(5, 0) PASSED
    ------

    >>> test_extreme()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) FAILED: expected Color(red=0, green=0, blue=255),\
    got Color(red=0, green=0, blue=25)
    ------
    Checking pixel @(4, 0) PASSED
    ------
    Checking pixel @(5, 0) PASSED
    ------
    """
    original = create_image(6, 1)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 1))
    set_color(original, 2, 0, create_color(127, 127, 127))
    set_color(original, 3, 0, create_color(125, 73, 224))
    set_color(original, 4, 0, create_color(254, 255, 255))
    set_color(original, 5, 0, create_color(255, 255, 255))

    expected = create_image(6, 1)
    set_color(expected, 0, 0, create_color(0, 255, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 255))
    set_color(expected, 4, 0, create_color(255, 255, 255))
    set_color(expected, 5, 0, create_color(255, 255, 255))

    extreme_image = extreme_contrast(original)
    for x, y, col in extreme_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_vertical_flip():
    """
    Author: Siddharth Natamai - 101143016
    Tests the flip_vertical function.

    >>> test_vertical_flip()
    """

    # Create a image with a resolution of 4x2 (8 pixels in total)
    original = create_image(4, 2)
    set_color(original, 0, 0, create_color(0, 0, 0))
    set_color(original, 1, 0, create_color(0, 0, 0))
    set_color(original, 2, 0, create_color(255, 255, 255))
    set_color(original, 3, 0, create_color(255, 255, 255))
    set_color(original, 0, 1, create_color(0, 0, 0))
    set_color(original, 1, 1, create_color(0, 0, 0))
    set_color(original, 2, 1, create_color(255, 255, 255))
    set_color(original, 3, 1, create_color(255, 255, 255))

    # Expected image after passing into the flip_vertical function.
    expected = create_image(4, 2)
    set_color(expected, 0, 0, create_color(255, 255, 255))
    set_color(expected, 1, 0, create_color(255, 255, 255))
    set_color(expected, 2, 0, create_color(0, 0, 0))
    set_color(expected, 3, 0, create_color(0, 0, 0))
    set_color(expected, 0, 1, create_color(255, 255, 255))
    set_color(expected, 1, 1, create_color(255, 255, 255))
    set_color(expected, 2, 1, create_color(0, 0, 0))
    set_color(expected, 3, 1, create_color(0, 0, 0))

    flipped_image = flip_vertical(original)

    # Checks each pixel and prints 'PASSED' or 'FAILED' based on expected
    # image values and image passed into flip_vertical
    for x, y, col in flipped_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                    col, get_color(expected, x, y))


def test_three_tone(original_image: Image):
    """ Author: Siddharth Natamai - 101143016
        Date: Nov 17, 2019

        Returns a bool depending on whether the the function is working
        properly or not
        >>> test_three_tone()
        True
        >>> test_three_tone()
        False
    """
    filtered_image = three_tone(original_image, "black", "white", "lime")
    test_state = True

    for pixel in filtered_image:
        x, y, (r, g, b) = pixel
        color_original = get_color(original_image, x, y)
        color_filtered = get_color(filtered_image, x, y)
        color_average = (color_original[0] + color_original[1] +
                         color_original[2]) // 3

        colour_1 = create_color(0, 0, 0)
        colour_2 = create_color(255, 255, 255)
        colour_3 = create_color(0, 255, 0)

        test_state = bool(
            (color_average <= 84 and color_filtered == colour_1)
            or ((84 < color_average <= 170) and color_filtered == colour_2)
            or (color_average >= 171 and color_filtered == colour_3))

    if test_state:
        print('Test Passed')
    else:
        print('Test Failed')

    return test_state


def test_two_tone(original_image: Image):
    """ Author: Siddharth Natamai - 101143016
        Date: Nov 17, 2019

        Returns a bool depending on whether the the function is working
        properly or not.
        >>> test_two_tone()
        True
        >>> test_two_tone()
        False
        """
    filtered_image = tt(original_image, "black", "white")
    test_state = True

    for pixel in filtered_image:
        x, y, (r, g, b) = pixel
        color_original = get_color(original_image, x, y)
        color_filtered = get_color(filtered_image, x, y)
        color_average = (color_original[0] + color_original[1] +
                         color_original[2]) // 3

        colour_1 = create_color(0, 0, 0)
        colour_2 = create_color(255, 255, 255)

        if color_average <= 127 and color_filtered == colour_1 \
                or color_average >= 128 and color_filtered == colour_2:
            test_state = True
        else:
            test_state = False

    if test_state:
        print('Test Passed')
    else:
        print('Test Failed')

    return test_state


def test_sepia() -> None:
    """Returns the information on whether or not the sepia filter works
    properly or not. The function returns the pixels that have passed the
    test. All pixels have to pass in order to confirm the success of the
    sepia filter. Otherwise, the filter does not work properly.

    - Function written by Malak Abdou - 101139692

    >>> test_sepia()
    (0,0) PASSED
    (1,0) PASSED
    (2,0) PASSED
    (3,0) PASSED
    (0,1) PASSED
    (1,1) PASSED
    (2,1) PASSED
    (3,1) PASSED

    References: check_equal function from fib2.py, provided by ECOR 1051
    staff.
    """
    original = create_image(4, 2)

    set_color(original, 0, 0, create_color(15, 250, 8))
    set_color(original, 1, 0, create_color(8, 20, 11))
    set_color(original, 2, 0, create_color(5, 55, 15))
    set_color(original, 3, 0, create_color(32, 206, 56))

    set_color(original, 0, 1, create_color(93, 51, 240))
    set_color(original, 1, 1, create_color(11, 23, 41))
    set_color(original, 2, 1, create_color(54, 26, 190))
    set_color(original, 3, 1, create_color(21, 68, 49))

    expected = create_image(4, 2)

    set_color(expected, 0, 0, create_color(104.65, 91, 77.35))
    set_color(expected, 1, 0, create_color(14.3, 13, 11.7))
    set_color(expected, 2, 0, create_color(27.5, 25, 22.5))
    set_color(expected, 3, 0, create_color(112.7, 98, 83.3))

    set_color(expected, 0, 1, create_color(147.2, 128, 108.8))
    set_color(expected, 1, 1, create_color(27.5, 25, 22.5))
    set_color(expected, 2, 1, create_color(103.5, 90, 76.5))
    set_color(expected, 3, 1, create_color(50.6, 46, 41.4))

    sepia_image = sepia(original)

    for x, y, color in sepia_image:
        check_equal('(' + str(x) + ',' + str(y) + ')', color,
                    get_color(expected, x, y))

    def test_detect_edges_better() -> None:
        """Returns the information on whether or not the filter
        detect_edges_better works properly or not. The function returns the
        pixels that have passed the test. All pixels have to pass in order to
        confirm the success of the detect_edges_better filter. Otherwise, the
        filter does not work properly.

        -Function written by Malak Abdou - 101139692

        >>> test_detect_edges_better()
        (0,0) PASSED
        (1,0) PASSED
        (2,0) PASSED
        (3,0) PASSED
        (0,1) PASSED
        (1,1) PASSED
        (2,1) PASSED
        (3,1) PASSED

        References: check_equal function from fib2.py, provided by ECOR 1051
        staff.
        """

        black = create_color(0, 0, 0)
        white = create_color(255, 255, 255)

        original = create_image(4, 2)

        set_color(original, 0, 0, create_color(15, 250, 7))
        set_color(original, 1, 0, create_color(8, 19, 10))
        set_color(original, 2, 0, create_color(5, 55, 15))
        set_color(original, 3, 0, create_color(32, 206, 56))

        set_color(original, 0, 1, create_color(43, 50, 21))
        set_color(original, 1, 1, create_color(11, 23, 40))
        set_color(original, 2, 1, create_color(54, 26, 190))
        set_color(original, 3, 1, create_color(21, 68, 48))

        expected = create_image(4, 2)

        set_color(expected, 0, 0, create_color(0, 0, 0))
        set_color(expected, 1, 0, create_color(255, 255, 255))
        set_color(expected, 2, 0, create_color(0, 0, 0))
        set_color(expected, 3, 0, create_color(0, 0, 0))

        set_color(expected, 0, 1, create_color(255, 255, 255))
        set_color(expected, 1, 1, create_color(0, 0, 0))
        set_color(expected, 2, 1, create_color(0, 0, 0))
        set_color(expected, 3, 1, create_color(255, 255, 255))

        threshold = 15  # Assume threshold chosen is 15.

        edges_image = detect_edges_better(original, threshold)

        for x, y, color in edges_image:
            check_equal('(' + str(x) + ',' + str(y) + ')', color,
                        get_color(expected, x, y))
