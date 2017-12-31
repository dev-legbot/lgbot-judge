import sys

from logging import getLogger
from logging import INFO
from logging import StreamHandler


_log = None
_log = getLogger(__name__)
_log.setLevel(INFO)
_log.flush = sys.stdout.flush
handler = StreamHandler(sys.stdout)
_log.addHandler(handler)


def logger():
    return _log
