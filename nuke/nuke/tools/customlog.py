import inspect
import logging
import sys

rootLogger = logging.getLogger()
rootLogger.setLevel(logging.DEBUG)

FORMAT = '[%(name)s:%(funcName)s:%(lineno)d] [%(asctime)s] %(levelname)s %(message)s'

class CustomFormatter(logging.Formatter):
    def __init__(self, fmt):
        self.basestack = None
        logging.Formatter.__init__(self, fmt)

    def format(self, r):
        # Whatever we're called at first, that's 0.
        if self.basestack is None:
            self.basestack = len(inspect.stack())
        indent = " " * (len(inspect.stack()) - self.basestack)
        msg = logging.Formatter.format(self, r)
        return "\n".join([indent + x for x in msg.split("\n")])


streamHandler = logging.StreamHandler(sys.stderr)
streamHandler.setLevel(logging.DEBUG)
streamHandler.setFormatter(CustomFormatter(FORMAT))
rootLogger.addHandler(streamHandler)

log = logging.getLogger (__name__)
log.info('log handler initialized')

