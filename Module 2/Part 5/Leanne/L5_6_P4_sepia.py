from simple_Cimpl_filters import *
from Cimpl import *

def sepia(original_image: Image) -> Image:
    """Returns a black and white image which has been tinted yellow.
    -Function written by Leanne Matamoros - 101147405
    
    >>> original_image= load_image(choose_file())
    >>> sepia(original_image)
    <Cimpl.Image object at 0x00000212C566DD88>
    
    """
    new_image = copy(original_image)
    sepia_filter = grayscale(new_image)

    for pixel in sepia_filter:
        x, y, (r, g, b) = pixel
        if r < 63:
            r *= 1.1
            b *= 0.9
            
        if (63 <= r <= 191):
            r *= 1.15
            b *= 0.85
            
        if (r > 191):
            r *= 1.08
            b *= 0.93
            
        new_color = create_color(r, g, b)
        set_color(sepia_filter, x, y, new_color)
        
    return sepia_filter
