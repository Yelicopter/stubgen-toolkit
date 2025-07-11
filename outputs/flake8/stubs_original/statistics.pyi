from collections.abc import Generator
from typing import Any, List, NamedTuple, Optional

class Key(NamedTuple):
    filename: str
    code: str

class Statistic:
    error_code: str
    filename: str
    message: str
    count: int

class Statistics:
    def __init__(self) -> None: ...
    def error_codes(self) -> List[str]: ...
    def record(self, error: Any) -> None: ...
    def statistics_for(self, prefix: str, filename: Optional[str] = ...) -> Generator[Statistic, None, None]: ...
