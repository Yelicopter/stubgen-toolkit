import functools
import linecache
import logging
from re import Match
from typing import NamedTuple, Optional

LOG: logging.Logger

@functools.lru_cache(maxsize=512)
def _find_noqa(physical_line: str) -> Optional[Match[str]]: ...

class Violation(NamedTuple):
    code: str
    filename: str
    line_number: int
    column_number: int
    text: str
    physical_line: Optional[str]
    
    def is_inline_ignored(self, disable_noqa: bool) -> bool: ...