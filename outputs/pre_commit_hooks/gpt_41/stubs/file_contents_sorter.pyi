from typing import Sequence, Optional, Callable, IO, Any

PASS: int
FAIL: int

def sort_file_contents(
    f: IO[bytes],
    key: Callable[[bytes], Any] = ...,
    *,
    unique: bool = ...,
) -> int: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...