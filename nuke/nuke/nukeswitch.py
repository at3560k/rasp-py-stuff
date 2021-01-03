#!/usr/bin/env python

# pylint: disable=missing-docstring

import RPi.GPIO as GPIO
import time

from customlog import logging
LOG = logging.getLogger(__name__)

GREEN_BTN = 27
SWITCH_CHAIN = 17

POST_BLINK = 3
POST_ON = 0.25
POST_OFF = 0.25
POLL_TIME = 15

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SWITCH_CHAIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(GREEN_BTN, GPIO.OUT)

    # 1 open, 0 closed.

def teardown():
    GPIO.cleanup()

def readbtn(pin):
    i = GPIO.input(pin)
    return i

def post():
    for _ in range(POST_BLINK):
        GPIO.output(GREEN_BTN, True)
        time.sleep(POST_ON)
        GPIO.output(GREEN_BTN, False)
        time.sleep(POST_OFF)


def blink():
    for _ in range(2):
        GPIO.output(GREEN_BTN, True)
        time.sleep(3)
        GPIO.output(GREEN_BTN, False)
        time.sleep(1)

def main():
    setup()
    post()
    for _ in range(POLL_TIME):
        active = not readbtn(SWITCH_CHAIN)
        LOG.info("Active: %s", active)
        if active:
            LOG.info('Illuminating')
            blink()
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    finally:
        teardown()

