import sys

from logging import getLogger
from logging import Formatter
from logging import INFO
from logging import StreamHandler


loggers = {}


class Logger(object):
    def __init__(self, name):
        global loggers

        if loggers.get(name):
            self._log = loggers.get(name)
            return

        logger = getLogger(name)
        logger.setLevel(INFO)
        logger.flush = sys.stdout.flush
        handler = StreamHandler(sys.stdout)
        formatter = Formatter("%(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        loggers.update(dict(name=logger))
        self._log = logger

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
