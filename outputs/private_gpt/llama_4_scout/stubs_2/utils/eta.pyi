import datetime
import logging
import math
import time
from collections import deque
from typing import Any

def human_time(*args: Any, **kwargs: Any) -> str:
    ...

def eta(iterator: Any) -> Any:
    ...

class ETA:
    def __init__(self, total: int) -> None:
        ...

    def human_time(self) -> str:
        ...

    def update(self, count: int) -> None:
        ...

    def needReport(self, whenSecs: int) -> bool:
        ...

    def _calc(self) -> bool:
        ...