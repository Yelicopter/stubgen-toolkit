from collections.abc import Iterable as Iterable, Sequence
from typing import Any, Callable, IO

PASS: int
FAIL: int

def sort_file_contents(f: IO[bytes], key: Callable[[bytes], Any], *, unique: bool = ...) -> int: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
