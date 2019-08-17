# -*- coding: utf-8 -*-

import pytest

from unicorn.color import Color
from unicorn.fake_unicorn_hat import FakeUnicornHat
from unicorn.unicorn import Unicorn


@pytest.fixture(scope="module")
def unicorn_hat():
    return FakeUnicornHat()


@pytest.fixture(scope="module")
def color():
    return Color(hex='007F7F')


@pytest.fixture
def unicorn(color, unicorn_hat):
    return Unicorn(unicorn_hat, color)
