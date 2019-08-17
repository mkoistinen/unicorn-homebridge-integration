# -*- coding: utf-8 -*-

import abc


class EffectBase(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, uh):
        self.uh = uh
        self.width, self.height = self.uh.get_shape()

    def paint_all(self, r, g, b):
        for x in range(self.width):
            for y in range(self.height):
                self.uh.set_pixel(x, y, r, g, b)
        self.uh.show()

    @abc.abstractmethod
    def run(self, stop):
        pass
