from collections.abc import Sequence
from typing import Any, Callable, IO

PASS: int
FAIL: int

def sort_file_contents(f: IO[bytes], key: Callable[[bytes], Any] | None, *, unique: bool = ...) -> int: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
