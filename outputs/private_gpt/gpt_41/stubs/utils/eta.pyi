import datetime
import logging
import math
import time
from collections import deque
from typing import Any, Iterator

logger: logging.Logger

def human_time(*args: Any, **kwargs: Any) -> str: ...
def eta(iterator: list[Any]) -> Iterator[Any]: ...

class ETA:
    total: int
    rate: float
    _timing_data: deque[tuple[float, int]]
    secondsLeft: float
    nexttime: float

    def __init__(self, total: int): ...
    def human_time(self) -> str: ...
    def update(self, count: int) -> None: ...
    def needReport(self, whenSecs: int) -> bool: ...
    def _calc(self) -> bool: ...