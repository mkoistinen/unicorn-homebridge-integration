# -*- coding: utf-8 -*-

import pytest

from unicorn.color import Color


@pytest.mark.parametrize("hex_code,rgb_tuple", [
    ('000000', (0, 0, 0)),
    ('FFFFFF', (255, 255, 255)),
    ('ff9429', (255, 148, 41)),
    ('00a2Ff', (0, 162, 255)),
    ('fF2977', (255, 41, 119)),
])
def test_create_from_hex__valid_hex_codes(hex_code, rgb_tuple):
    assert Color(hex=hex_code).as_rgb() == rgb_tuple


@pytest.mark.parametrize("bad_hex_code", [
    '0000',
    'ffgghh',
    'abcdefg',
    123456,
])
def test_create_from_hex__invalid_hex_codes(bad_hex_code):
    try:
        Color(hex=bad_hex_code)
    except AttributeError:
        pass


@pytest.mark.parametrize("rgb_tuple,hex_code", [
    ((0, 0, 0), '000000'),
    ((255, 255, 255), 'FFFFFF'),
    ((255, 148, 41), 'FF9429'),
    ((0, 162, 255), '00A2FF'),
    ((255, 41, 119), 'FF2977'),
])
def test_create_from_rgb__valid_rgb(rgb_tuple, hex_code):
    r, g, b = rgb_tuple
    c = Color(r=r, g=g, b=b)
    assert c.as_hex() == hex_code.upper()


@pytest.mark.parametrize("bad_rgb", [
    (1, 23, 45, 67),
    (16, 32),
])
def test_create_from_rgb__invalid_rgb(bad_rgb):
    try:
        r, g, b = bad_rgb
        c = Color(r=r, g=g, b=b)
        if c.as_hex() != '000000':
            pytest.fail('This should not have worked: {}'.format(c.as_hex()))
    except ValueError:
        pass


@pytest.mark.parametrize("hsv_tuple,hex_code", [
    ((0, 0, 0), '000000'),
    ((0, 0, 100), 'FFFFFF'),
    ((30, 84, 100), 'FF9429'),
    ((202, 100, 100), '00A2FF'),
    ((338, 84, 100), 'FF2977'),
])
def test_create_from_hsv__valid_hsv(hsv_tuple, hex_code):
    h, s, v = hsv_tuple
    c = Color(h=h, s=s, v=v)
    assert c.as_hex() == hex_code.upper()


def test_create__unexpected_input():
    c = Color(r=27)
    assert c.as_hex() == '000000'


@pytest.mark.parametrize("hex_code,hsv_tuple", [
    ('000000', (0, 0, 0)),
    ('FFFFFF', (0, 0, 100)),
    ('FF9429', (30, 84, 100)),
    ('00A2FF', (202, 100, 100)),
    ('FF2977', (338, 84, 100)),
])
def test_as_hsv(hex_code, hsv_tuple):
    hsv = Color(hex=hex_code).as_hsv()
    new_hsv = tuple(int(hsv[c] + 0.5) for c in range(3))
    assert new_hsv == hsv_tuple


@pytest.mark.parametrize("hex_code,brightness", [
    ('000000', 0),
    ('FFFFFF', 100),
    ('2F9429', 58),
    ('00527F', 49),
    ('293F77', 46),
])
def test_brightness(hex_code, brightness):
    assert Color(hex=hex_code).brightness == brightness
