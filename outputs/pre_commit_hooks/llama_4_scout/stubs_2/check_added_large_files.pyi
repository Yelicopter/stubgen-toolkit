from __future__ import annotations

import argparse
import math
import os
import subprocess
from collections.abc import Sequence
from pre_commit_hooks.util import added_files
from pre_commit_hooks.util import zsplit

def filter_lfs_files(filenames: Sequence[str]) -> None:
    ...

def find_large_added_files(
    filenames: Sequence[str],
    maxkb: int,
    *,
    enforce_all: bool = False,
) -> int:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...