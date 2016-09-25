#!/usr/bin/env python

# pylint: disable=missing-docstring

import RPi.GPIO as GPIO
import time

def setup(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)

def teardown():
    GPIO.cleanup()

def readbtn(pin):
    i = GPIO.input(pin)
    return i


def main():
    pin = 26
    setup(pin)
    for i in range(10):
        print readbtn(pin)
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    finally:
        teardown()

