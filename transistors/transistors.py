#!/usr/bin/env python

# better/simpler than rpi.gpio ?
import RPi.GPIO as GPIO
import time

# DO NOT power both!
ON_COLLECTOR = 19 # 17
OFF_COLLECTOR = 16 # 21

DURATION=0.5

def setup():
    GPIO.setmode(GPIO.BCM)
    for i in (ON_COLLECTOR, OFF_COLLECTOR):
        GPIO.setup(i, GPIO.OUT)
    stopAll()

def teardown():
    stopAll()
    GPIO.cleanup()

def stopAll():
    for i in (ON_COLLECTOR, OFF_COLLECTOR):
        GPIO.output(i, False)

def signal(pin: int, duration=DURATION):
    """
    Send a signal to a switch for N seconds
    """
    GPIO.output(pin, True)
    time.sleep(DURATION)
    GPIO.output(pin, False)

def powerOn():
    signal(ON_COLLECTOR)
    print("on")


def powerOff():
    signal(OFF_COLLECTOR)
    print("off")

def main():
    from IPython import embed
    embed()

if __name__ == '__main__':
    try:
        setup()
        main()
    finally:
        teardown()
