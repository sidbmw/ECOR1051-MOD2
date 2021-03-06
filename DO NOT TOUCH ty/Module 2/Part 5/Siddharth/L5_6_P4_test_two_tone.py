from Cimpl import get_color, create_color, Image
from L5_6_P4_two_tone import two_tone as tt


# file = choose_file()
# original_image = load_image(file)


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

# show(tt(original_image, "black", "white"))

# test_two_tone()
