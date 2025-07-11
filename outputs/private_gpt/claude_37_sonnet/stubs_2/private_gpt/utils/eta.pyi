import datetime
import logging
import math
import time
from collections import deque
from typing import Any, Generator, Iterator, List, Tuple

logger: logging.Logger

def human_time(*args: Any, **kwargs: Any) -> str: ...
def eta(iterator: List[Any]) -> Generator[Any, None, None]: ...

class ETA:
    def __init__(self, total: int):
        self.total: int
        self.rate: float
        self._timing_data: deque[Tuple[float, int]]
        self.secondsLeft: float
        self.nexttime: float
    
    def human_time(self) -> str: ...
    def update(self, count: int) -> None: ...
    def needReport(self, whenSecs: int) -> bool: ...
    def _calc(self) -> bool: ...