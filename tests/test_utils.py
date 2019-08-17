# -*- coding: utf-8 -*-

import pytest

from unicorn.utils import (
    bracket, hex_to_rgb, get_rgb_brightness, set_rgb_brightness, transition
)


@pytest.mark.parametrize('value,low,high,result', (
        (128, 0, 255, 128),
        (128, 0, 100, 100),
        (-99, 0, 255, 0),
        (1.2, 0, 255, 1.2),
        (-5, -10, 100, -5),
))
def test_bracket(value, low, high, result):
    assert bracket(value, low=low, high=high) == result


@pytest.mark.parametrize('step,result', (
    (0, (0, 0, 0)),
    (50, (127, 127, 127)),
    (100, (255, 255, 255)),
))
def test_transition(step, result):
    new_rgb = transition(0, 0, 0, 255, 255, 255, step, 100)
    new_rgb = tuple(int(c + 0.5) for c in new_rgb)
    assert new_rgb == result


@pytest.mark.parametrize("hex_code,rgb_tuple", [
    ('000000', (0, 0, 0)),
    ('FFFFFF', (255, 255, 255)),
    ('ff9429', (255, 148, 41)),
    ('00a2Ff', (0, 162, 255)),
    ('fF2977', (255, 41, 119)),
])
def test_hex_to_rgb(hex_code, rgb_tuple):
    assert hex_to_rgb(hex_code) == rgb_tuple


@pytest.mark.parametrize("hex_code,brightness", [
    ('000000', 0),
    ('FFFFFF', 100),
    ('2F9429', 58),
    ('00527F', 49),
    ('293F77', 46),
])
def test_rgb_brightness(hex_code, brightness):
    assert int(get_rgb_brightness(hex_code)) == brightness


@pytest.mark.parametrize("hex_code,brightness,new_rgb", [
    ('000000', 10, (26, 26, 26)),
    ('FFFFFF', 90, (230, 230, 230)),
    ('2F9429', 20, (16, 51, 14)),
    ('00527F', 80, (0, 132, 204)),
    ('293F77', 50, (44, 67, 128)),
])
def test_set_rgb_brightness(hex_code, brightness, new_rgb):
    assert set_rgb_brightness(hex_code, brightness) == new_rgb
