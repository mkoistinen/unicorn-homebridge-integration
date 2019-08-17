# -*- coding: utf-8 -*-

from random import randint
from time import sleep

from unicorn.utils import transition
from base import EffectBase


class CandleLight(EffectBase):
    """
    Simulates a lit candle.
    """
    def __init__(self, *args, **kwargs):
        self.old_r, self.old_g, self.old_b = 0, 162, 255
        self.min_steps, self.max_steps = 10, 50
        super(CandleLight, self).__init__(*args, **kwargs)

    def run(self, stop):
        while True:
            r = randint(192, 255 - 16)
            g = r - 96 + randint(0, 8) - 4
            b = 0

            steps = randint(self.min_steps, self.max_steps)
            for t in range(steps):
                nr, ng, nb = transition(
                    r, g, b,
                    self.old_r, self.old_g, self.old_b,
                    t, steps
                )
                self.paint_all(int(nr), int(ng), int(nb))
                if stop():
                    return
                sleep(0.01)

            self.old_r, self.old_g, self.old_b = r, g, b
