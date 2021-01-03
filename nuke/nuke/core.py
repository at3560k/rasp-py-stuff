#!/usr/bin/env python

""" Implements nuke program """

import RPi.GPIO as GPIO
import time

from tools.customlog import logging
LOG = logging.getLogger(__name__)

from config import NukeConfig

__all__ = ['main', 'runmodule', 'NBox']

class NBox(object):
    """ I am the physical box """

    def __init__(self, config=None):
        if config is None:
            config = NukeConfig
        self.config = config

        self.__setup()
        self.post()


    def post(self):
        LOG.info("POSTing...")
        for _ in xrange(self.config.POST_BLINK):
            GPIO.output(self.config.GREEN_BTN, True)
            time.sleep(self.config.POST_ON)
            GPIO.output(self.config.GREEN_BTN, False)
            time.sleep(self.config.POST_OFF)

    def __setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.config.SWITCH_CHAIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.config.GREEN_BTN, GPIO.OUT)
        # 1 open, 0 closed

    def __teardown(self):
        GPIO.cleanup()

def runmodule(name='__main__', **kw):
    """Collect and run tests in a single module only. Defaults to running
    tests in __main__. Additional arguments to TestProgram may be passed
    as keyword arguments.
    """
    main(**kw)


main = NBox

if __name__ == '__main__':
    main()
