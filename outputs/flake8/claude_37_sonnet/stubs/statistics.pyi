from __future__ import annotations

from collections.abc import Generator
from typing import NamedTuple, Optional

from flake8.violation import Violation

class Statistics:
    _store: dict[Key, Statistic]

    def __init__(self) -> None: ...
    def error_codes(self) -> list[str]: ...
    def record(self, error: Violation) -> None: ...
    def statistics_for(
        self, prefix: str, filename: Optional[str] = None
    ) -> Generator[Statistic, None, None]: ...

class Key(NamedTuple):
    filename: str
    code: str

    @classmethod
    def create_from(cls, error: Violation) -> Key: ...
    def matches(self, prefix: str, filename: Optional[str]) -> bool: ...

class Statistic:
    error_code: str
    filename: str
    message: str
    count: int

    def __init__(
        self, error_code: str, filename: str, message: str, count: int
    ) -> None: ...
    @classmethod
    def create_from(cls, error: Violation) -> Statistic: ...
    def increment(self) -> None: ...