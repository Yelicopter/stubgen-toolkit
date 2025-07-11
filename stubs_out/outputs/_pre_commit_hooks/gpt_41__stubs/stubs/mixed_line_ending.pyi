from typing import Optional, Sequence

CRLF: bytes
LF: bytes
CR: bytes
ALL_ENDINGS: tuple[bytes, ...]
FIX_TO_LINE_ENDING: dict[str, bytes]

def fix_filename(filename: str, fix: str) -> int: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...
