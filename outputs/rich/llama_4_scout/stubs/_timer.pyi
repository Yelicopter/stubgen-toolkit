"""
Timer context manager, only used in debug.

"""

from time import time

import contextlib
from typing import Generator


@contextlib.contextmanager
def timer(subject: str = "time") -> Generator:
    """print the elapsed time. (only used in debugging)"""
    ...