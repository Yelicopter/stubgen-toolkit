from collections.abc import Iterable as Iterable, Sequence
from typing import Any, Callable, IO, Optional

PASS: int
FAIL: int

def sort_file_contents(f: IO[bytes], key: Optional[Callable[[bytes], Any]], *, unique: bool = ...) -> int: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...
