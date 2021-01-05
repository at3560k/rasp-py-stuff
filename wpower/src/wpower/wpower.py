"""
Outlet module - presently a singleton per on/off
"""

# Note: module only runs on a raspy, expect a thousand syntax errors in any IDE
# trying to dynamically eval :(

import time

import RPi.GPIO as GPIO

# DO NOT power both!
ON_COLLECTOR = 19
OFF_COLLECTOR = 16

DURATION = 0.5


def setup():
    """
    Setup pins for stable
    """
    GPIO.setmode(GPIO.BCM)
    for i in (ON_COLLECTOR, OFF_COLLECTOR):
        GPIO.setup(i, GPIO.OUT)
    stop_all()


def teardown():
    stop_all()
    GPIO.cleanup()


def stop_all():
    """
    Ensure all outputs are off
    """
    for i in (ON_COLLECTOR, OFF_COLLECTOR):
        GPIO.output(i, False)


def signal(pin: int, duration=DURATION):
    """
    Send a signal to a switch for N seconds
    """
    GPIO.output(pin, True)
    time.sleep(DURATION)
    GPIO.output(pin, False)


def power_on():
    signal(ON_COLLECTOR)
    print("on")


def power_off():
    signal(OFF_COLLECTOR)
    print("off")
