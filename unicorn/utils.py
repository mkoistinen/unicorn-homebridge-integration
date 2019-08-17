# -*- coding: utf-8 -*-

import logging
from colorsys import hsv_to_rgb, rgb_to_hsv

RGB_ERROR_COLOR = 255, 127, 127

logger = logging.getLogger('unicorn.utils')


def bracket(v, low=0, high=255):
    """Simply brackets a value between 0 and 255."""
    return max(low, min(high, v))


def transition(r, g, b, old_r, old_g, old_b, step, steps):
    """Utility method for interpolating."""
    vr = r + (old_r - r) / float(steps) * float(step)
    vg = g + (old_g - g) / float(steps) * float(step)
    vb = b + (old_b - b) / float(steps) * float(step)
    return bracket(vr), bracket(vg), bracket(vb)


def hex_to_rgb(value):
    """
    Convert hex formatted color to tuple of 3 integers from 0 - 255.
    """
    value = value.lstrip('#')
    length = len(value)

    try:
        assert length == 3 or length == 6
        triplet = tuple(
            bracket(int(value[i:i + length / 3], 16))
            for i in range(0, length, length / 3)
        )
        return triplet
    except AssertionError:
        logger.exception(
            'Unexpected number of digits in hex value: "{}"'.format(value))
        return RGB_ERROR_COLOR
    except ValueError:
        logger.exception(
            'Unable to convert hex "{}" to decimal'.format(value))
        return RGB_ERROR_COLOR


def get_rgb_brightness(color):
    """
    Given an RGB _color (hex format), return it's brightness.
    """
    r, g, b = hex_to_rgb(color)
    hsv = rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    return hsv[2] * 100


def set_rgb_brightness(color, brightness):
    """
    Given an RGB _color (hex format) and brightness, return a new RGB _color.
    :param color: hex format RGB _color string
    :param brightness: Integer from 0 to 100
    """
    r, g, b = hex_to_rgb(color)
    hsv = rgb_to_hsv(r/255.0, g/255.0, b/255.0)
    rgb = hsv_to_rgb(hsv[0], hsv[1], brightness/100.0)
    return (
        int(rgb[0] * 255.0 + 0.5),
        int(rgb[1] * 255.0 + 0.5),
        int(rgb[2] * 255.0 + 0.5),
    )
