from _typeshed import Incomplete
from collections.abc import Sequence
from typing import Optional

CRLF: bytes
LF: bytes
CR: bytes
ALL_ENDINGS: Incomplete
FIX_TO_LINE_ENDING: Incomplete

def fix_filename(filename: str, fix: str) -> int: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...
