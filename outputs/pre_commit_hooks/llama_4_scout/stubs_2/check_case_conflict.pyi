from __future__ import annotations

import argparse
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Sequence

from pre_commit_hooks.util import added_files
from pre_commit_hooks.util import cmd_output

def lower_set(iterable: Iterable[str]) -> set[str]:
    ...

def parents(file: str) -> Iterator[str]:
    ...

def directories_for(files: Sequence[str]) -> set[str]:
    ...

def find_conflicting_filenames(filenames: Sequence[str]) -> int:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...