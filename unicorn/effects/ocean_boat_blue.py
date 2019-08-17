# -*- coding: utf-8 -*-

import math
from time import sleep

from unicorn.utils import bracket
from base import EffectBase


class OceanBoatBlue(EffectBase):
    """
    This is a slowly undulating and ocean blue effect.
    """
    def run(self, stop):
        while True:
            for d in range(360):
                a = math.sin(d / (2 * math.pi))
                r = 0
                g = 121 + a * 41
                b = 191 + a * 64

                self.paint_all(
                    bracket(int(r)),
                    bracket(int(g)),
                    bracket(int(b))
                )
                if stop():
                    return
                sleep(0.2)
