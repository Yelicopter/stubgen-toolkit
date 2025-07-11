from typing import Sequence, Optional

def _fix_file(
    filename: str,
    is_markdown: bool,
    chars: Optional[bytes],
) -> bool: ...
def _process_line(
    line: bytes,
    is_markdown: bool,
    chars: Optional[bytes],
) -> bytes: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...