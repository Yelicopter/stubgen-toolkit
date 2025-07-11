from typing import Sequence, Optional

CRLF: bytes
LF: bytes
CR: bytes
ALL_ENDINGS: tuple[bytes, ...]
FIX_TO_LINE_ENDING: dict[str, bytes]

def _fix(filename: str, contents: bytes, ending: bytes) -> None: ...
def fix_filename(filename: str, fix: str) -> int: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...