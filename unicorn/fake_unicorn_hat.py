# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class FakeUnicornHat:
    PHAT = object

    def __init__(self, *args, **kwargs):
        pass

    def set_layout(self, *args, **kwargs):
        pass

    def get_shape(self, *args, **kwargs):
        return 4, 8

    def set_pixel(self, *args, **kwargs):
        pass

    def show(self, *args, **kwargs):
        pass

    def clear(self, *args, **kwargs):
        pass


unicornhat = FakeUnicornHat()
