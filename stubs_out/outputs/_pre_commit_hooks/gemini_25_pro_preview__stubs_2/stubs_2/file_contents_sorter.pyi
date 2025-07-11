from collections.abc import Sequence
from typing import Any, Callable, Final, IO

PASS: Final[int]
FAIL: Final[int]

def sort_file_contents(f: IO[bytes], key: Callable[[bytes], Any] | None, *, unique: bool = ...) -> int: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
