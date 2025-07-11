from _typeshed import Incomplete as Incomplete
from collections.abc import Sequence

CRLF: bytes
LF: bytes
CR: bytes
ALL_ENDINGS: Incomplete
FIX_TO_LINE_ENDING: Incomplete

def fix_filename(filename: str, fix: str) -> int: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
