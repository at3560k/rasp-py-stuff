"""
Outlet module - presently a singleton per on/off
"""

import time
from typing import Optional, Set

# Note: module only runs on a raspy, expect a thousand syntax errors in any IDE
# trying to dynamically eval :(
import RPi.GPIO as GPIO

from wpower import settings


class Outlet:
    """
    Remote controlled outlet
    """

    _io_pins: Set[int] = set()
    _setup: bool = False

    def __init__(self, on: Optional[int] = None, off: Optional[int] = None):
        self._on = on
        self._off = off

        if not self.on:
            self._on = settings.DEFAULT_BCM_ON
        if not self.off:
            self._off = settings.DEFAULT_BCM_OFF

        Outlet._io_pins.update([self.on, self.off])
        self._setup()

    def _setup(self):
        """
        Setup pins for stable
        """
        if self._setup:
            return

        GPIO.setmode(GPIO.BCM)
        for i in (self.on, self.off):
            GPIO.setup(i, GPIO.OUT)
        self.stop_all()
        Outlet._setup = True

    @classmethod
    def _teardown(cls):
        """
        Make sure everything is disabled
        """
        for pin in cls._io_pins:
            GPIO.output(pin, False)

    @classmethod
    def _signal(cls, pin: int, duration: Optional[int] = None):
        """
        Send a signal to a switch for N seconds
        """

        if duration is None:
            duration = settings.DEFAULT_SWITCH_DURATION

        GPIO.output(pin, True)
        time.sleep(duration)
        GPIO.output(pin, False)

    @property
    def on(self):  # pylint: disable=invalid-name
        return self._on

    @property
    def off(self):
        return self._off

    def power_on(self):
        self._signal(self.on)

    def power_off(self):
        self._signal(self.off)
