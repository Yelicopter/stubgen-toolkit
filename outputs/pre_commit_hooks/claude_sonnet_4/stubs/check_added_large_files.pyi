from __future__ import annotations

import argparse
from collections.abc import Sequence

def filter_lfs_files(filenames: set[str]) -> None: ...

def find_large_added_files(
    filenames: Sequence[str],
    maxkb: int,
    *,
    enforce_all: bool = False,
) -> int: ...

def main(argv: Sequence[str] | None = None) -> int: ...