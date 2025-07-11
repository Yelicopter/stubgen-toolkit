from typing import Optional
from types import TracebackType

class timer:
    def __init__(self, subject: str = "time", console: Optional[object] = None) -> None: ...
    def __enter__(self) -> "timer": ...
    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> None: ...