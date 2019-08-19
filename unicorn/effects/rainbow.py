# -*- coding: utf-8 -*-

from math import cos, sin
import time

from unicorn.utils import bracket
from base import EffectBase


class Rainbow(EffectBase):
    """
    Largely borrowed from the Pimoromi examples.
    """
    i = 0.0
    offset = 30

    def __init__(self, *args, **kwargs):
        super(Rainbow, self).__init__(*args, **kwargs)

    def run(self, stop):
        while True:
            self.i = self.i + 0.3
            for y in range(self.height):
                for x in range(self.width):
                    r = (cos((x + self.i) / 2.0) + cos((y + self.i) / 2.0)) * 64.0 + 128.0
                    g = (sin((x + self.i) / 1.5) + sin((y + self.i) / 2.0)) * 64.0 + 128.0
                    b = (sin((x + self.i) / 2.0) + cos((y + self.i) / 1.5)) * 64.0 + 128.0

                    r = int(bracket(r + self.offset))
                    g = int(bracket(g + self.offset))
                    b = int(bracket(b + self.offset))
                    self.uh.set_pixel(x, y, r, g, b)
            if stop():
                return
            self.uh.show()
            time.sleep(0.02)
