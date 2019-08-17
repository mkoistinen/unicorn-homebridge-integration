# -*- coding: utf-8 -*-

from utils import bracket, hex_to_rgb, hsv_to_rgb, rgb_to_hsv


class Color:
    """
    Simply encapsulates the representation of a color.
    Internally, color is stored as an RGB 3-tuple
    """
    def __init__(self, **kwargs):
        """
        :param hex: 'RRGGBB'
        :param r: 0 - 255
        :param g: 0 - 255
        :param b: 0 - 255
        :param h: 0 - 360
        :param s: 0 - 100
        :param v: 0 - 100
        """
        if 'hex' in kwargs:
            hex_code = kwargs.get('hex')
            self._color = hex_to_rgb(hex_code)
        elif 'r' in kwargs and 'g' in kwargs and 'b' in kwargs:
            r = bracket(kwargs.get('r'))
            g = bracket(kwargs.get('g'))
            b = bracket(kwargs.get('b'))
            self._color = r, g, b
        elif 'h' in kwargs and 's' in kwargs and 'v' in kwargs:
            h = bracket(kwargs.get('h'), 0, 360)
            s = bracket(kwargs.get('s'), 0, 100)
            v = bracket(kwargs.get('v'), 0, 100)
            r, g, b = hsv_to_rgb(h/360.0, s/100.0, v/100.0)
            self._color = (
                int(r * 255.0 + 0.5),
                int(g * 255.0 + 0.5),
                int(b * 255.0 + 0.5)
            )
        else:
            self._color = 0, 0, 0

    def as_rgb(self):
        return self._color

    def as_hsv(self):
        r, g, b = self.as_rgb()
        h, s, v = rgb_to_hsv(r/255.0, g/255.0, b/255.0)
        return h * 360.0, s * 100.0, v * 100.0

    def as_hex(self):
        """Returns the color as a hex color."""
        r, g, b = self._color
        hex_color = ""
        for component in [int(r + 0.5), int(g + 0.5), int(b + 0.5)]:
            h = hex(component)[2:]
            if len(h) < 2:
                h = "0" + h
            hex_color += h
        return hex_color.upper()

    @property
    def brightness(self):
        """
        Gets the brightness of the color.
        :return: An integer from 0 to 100
        """
        h, s, v = self.as_hsv()
        return int(v)
