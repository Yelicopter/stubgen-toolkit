from typing import Sequence, Set, Optional

def filter_lfs_files(filenames: Set[str]) -> None: ...
def find_large_added_files(
    filenames: Sequence[str],
    maxkb: int,
    *,
    enforce_all: bool = ...,
) -> int: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...