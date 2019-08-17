# -*- coding: utf-8 -*-

import pytest

from unicorn.color import Color


def test_create(color, unicorn):
    assert unicorn._color == color
    assert unicorn._status is True


@pytest.mark.parametrize("truth", (True, False))
def test_set_status(unicorn, truth):
    unicorn.set_status(truth)
    assert unicorn.status == truth
    assert unicorn._status == truth


@pytest.mark.parametrize("new_color,truth", (
    ('123456', True),
    ('000000', False),
))
def test_set_color(unicorn, color, new_color, truth):
    assert unicorn.color == color
    unicorn.set_status(False)

    c = Color(hex=new_color)
    unicorn.set_color(c)
    assert unicorn.color == c
    assert unicorn.status == truth
