#!/usr/bin/env python

# pylint: disable=missing-docstring

import RPi.GPIO as GPIO
import time


# CONSTANTS
PHOTO_PIN = 21
LED_PIN = 22

THRESHOLD = 0.11
# 0.2 too big
# 0.1 too slow
DISCHARGE=0.1
MEASURE_ZZZ=0.05
HYSTERESIS_ZZZ=5 

RUN_TIME=60

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)

def teardown():
    GPIO.cleanup()

def discharge(pin):
    """ discharge capacitory"""
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(DISCHARGE)

def fill(pin):
    """ return when we're full"""
    GPIO.setup(pin, GPIO.IN)
    while GPIO.input(pin) == False: # potential infinite loop in bug circuit
        time.sleep(MEASURE_ZZZ)
    return

def measurefill_time(pin):
    """ fill capacitory, measure time"""
    discharge(pin)
    time_start = time.time()
    fill(pin)
    return time.time() - time_start

def main():
    setup()
    # run for one minute, cleanup
    time_end = time.time() + RUN_TIME

    while time.time() < time_end:
        fill_time = measurefill_time(PHOTO_PIN)

        if fill_time > THRESHOLD:
            print("dark, time:", fill_time)
            GPIO.output(LED_PIN, True)
        else:
            print("light, time:", fill_time)
            GPIO.output(LED_PIN, False)
        time.sleep(HYSTERESIS_ZZZ)



if __name__ == '__main__':
    try:
        main()
    finally:
        teardown()

