import logging

LOG = logging.getLogger(__name__)

class NukeConfig(object):
    GREEN_BTN = 27
    SWITCH_CHAIN = 17

    POST_BLINK = 3
    POST_ON = 0.25
    POST_OFF = 0.25
    POLL_TIME = 15

