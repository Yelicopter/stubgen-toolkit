from re import Match as Match
from typing import NamedTuple, Optional

class Violation(NamedTuple):
    code: str
    filename: str
    line_number: int
    column_number: int
    text: str
    physical_line: Optional[str]
    def is_inline_ignored(self, disable_noqa: bool) -> bool: ...
