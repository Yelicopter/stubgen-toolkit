import inspect
import logging
import sys
import time
from typing import List

from pydantic import BaseModel

from pandasai.helpers.telemetry import scarf_analytics

from .path import find_closest


class Log(BaseModel):
    pass


class Logger:
    _logs: List[Log]
    _logger: logging.Logger
    _verbose: bool
    _last_time: float

    def __init__(
        self, save_logs: bool = True, verbose: bool = False
    ) -> None:
        ...

    def log(self, message: str, level: int = logging.INFO) -> None:
        ...

    def _invoked_from(self, level: int = 5) -> str:
        ...

    def _calculate_time_diff(self) -> float:
        ...

    @property
    def logs(self) -> List[Log]:
        ...

    @property
    def verbose(self) -> bool:
        ...

    @verbose.setter
    def verbose(self, verbose: bool) -> None:
        ...

    @property
    def save_logs(self) -> bool:
        ...

    @save_logs.setter
    def save_logs(self, save_logs: bool) -> None:
        ...


scarf_analytics()