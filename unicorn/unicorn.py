# -*- coding: utf-8 -*-

import logging
from threading import Thread

logger = logging.getLogger('unicorn.unicorn')


class Unicorn:
    """
    This class represents a Unicorn PHAT and provides the API required
    """
    def __init__(self, uh, color, effect_modes=None):
        """
        Initialize the Unicorn PHAT
        :param uh: The Unicorn PHAT instance.
        :param color: A color instance to start with.
        :param effect_modes: a dictionary of colors and related effect classes.
        """
        # Prepare the lamp
        self._uh = uh
        self._uh.set_layout(uh.PHAT)
        self._width, self._height = self._uh.get_shape()

        # Initialize some instance vars
        self._color = None
        self._status = False

        # To support effects
        self._effect_modes = effect_modes if effect_modes else {}
        self._thread = None
        self._stop_threads = True

        # Turn it ON to the provided color
        self.set_color(color)

    def _stop_mode(self):
        """
        Stops any running effects.
        """
        if self._thread:
            self._stop_threads = True
            self._thread.join()
            self._thread = None
            self._stop_threads = False

    def _update(self):
        """
        Updates the color of the lamp, turning on any special effects or
        turning them off.
        """
        hex_color = self.color.as_hex()
        logger.info('Unicorn updating color to "{}".'.format(hex_color))
        if hex_color in self._effect_modes.keys():
            # Special colors with "modes", or animated effect that run in a loop
            # These are spawned off into a separate thread to keep running
            self._stop_mode()
            mode = self._effect_modes[hex_color](self._uh).run
            self._thread = Thread(target=mode,
                                  args=(lambda: self._stop_threads, ))
            self._thread.start()

        else:
            self._stop_mode()

            r, g, b = self.color.as_rgb()
            for x in range(self._width):
                for y in range(self._height):
                    self._uh.set_pixel(x, y, r, g, b)
            self._uh.show()

    @property
    def status(self):
        """Returns the current status (ON/OFF state)"""
        return self._status

    def set_status(self, status):
        """
        Turns the unicorn ON or OFF.
        :param status: Boolean (True == ON)
        """
        self._status = bool(status)
        if self._status:
            self._update()
        else:
            self._uh.clear()
            self._uh.show()

    @property
    def color(self):
        """Returns the current color."""
        return self._color

    def set_color(self, color):
        """
        Sets the color of the lamp.
        :param color: Color instance.
        """
        self._color = color
        if self._color.as_hex() != '000000':
            self.set_status(True)
        self._update()
