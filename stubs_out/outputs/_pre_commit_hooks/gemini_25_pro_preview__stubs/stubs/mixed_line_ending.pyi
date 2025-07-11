from collections.abc import Sequence
from typing import Final

CRLF: Final[bytes]
LF: Final[bytes]
CR: Final[bytes]
ALL_ENDINGS: Final[tuple[bytes, bytes, bytes]]
FIX_TO_LINE_ENDING: Final[dict[str, bytes]]

def fix_filename(filename: str, fix: str) -> bool: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
