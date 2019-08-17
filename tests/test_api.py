# -*- coding: utf-8 -*-

import mock
import pytest

from unicorn.api import unicorn
from unicorn.color import Color


from unicorn.api import (
    get_status, set_status, get_color, set_color,
    get_brightness, set_on, set_off,
)


def test_get_status():
    with mock.patch.object(unicorn, 'status', return_value=True):
        assert get_status() == '1'


@pytest.mark.parametrize('status,truth', [
    ('on', True),
    ('off', False),
    ('maybe', False)
])
def test_set_status(status, truth):
    unicorn.set_status(not truth)
    assert set_status(status) == "OK"
    assert unicorn.status == truth


def test_get_color():
    unicorn._color = Color(hex='123456')
    assert get_color() == '123456'


@pytest.mark.parametrize('hex_code,result', [
        ('123456', '123456'),
        ('#123456', '123456'),
])
def test_set_color(hex_code, result):
    set_color(hex_code)
    assert unicorn.color.as_hex() == result


@pytest.mark.parametrize('hex_code,brightness', [
    ('000000', '0'),
    ('FFFFFF', '100'),
    ('123456', '33'),
])
def test_get_brightness(hex_code, brightness):
    unicorn._color = Color(hex=hex_code)
    assert get_brightness() == brightness


def test_set_on():
    unicorn._status = False
    set_on()
    assert unicorn._status is True


def test_set_off():
    unicorn._status = True
    set_off()
    assert unicorn._status is False
