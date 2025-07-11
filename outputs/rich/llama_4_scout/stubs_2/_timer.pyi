from time import time
import contextlib
from typing import Generator

@contextlib.contextmanager
def timer(subject: str = "time") -> Generator[float, None, None]:
    """print the elapsed time. (only used in debugging)"""
    ...