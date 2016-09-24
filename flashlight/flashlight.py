#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)

def teardown():
    GPIO.cleanup()

def main():
    setup()
    GPIO.output(17, True)
    time.sleep(5)



if __name__ == '__main__':
    try:
        main()
    finally:
        teardown()

