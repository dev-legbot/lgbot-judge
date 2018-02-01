import sys

from logging import getLogger
from logging import INFO
from logging import StreamHandler


class Logger(object):
    def __init__(self):
        self._log = getLogger(__name__)
        self._log.setLevel(INFO)
        self._log.flush = sys.stdout.flush
        handler = StreamHandler(sys.stdout)
        self._log.addHandler(handler)

    def debug(self, msg, *arg, **kwards):
        self._log.debug(msg, *arg, **kwards)

    def info(self, msg, *arg, **kwards):
        self._log.info(msg, *arg, **kwards)

    def warning(self, msg, *arg, **kwards):
        self._log.warning(msg, *arg, **kwards)

    def error(self, msg, *arg, **kwards):
        self._log.error(msg, *arg, **kwards)

    def critical(self, msg, *arg, **kwards):
        self._log.critical(msg, *arg, **kwards)
