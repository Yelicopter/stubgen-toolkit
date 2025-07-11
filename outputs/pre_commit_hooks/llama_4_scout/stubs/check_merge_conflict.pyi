from __future__ import annotations

import argparse
import os.path
from collections.abc import Sequence

from pre_commit_hooks.util import cmd_output

CONFLICT_PATTERNS: list[bytes] = []

def is_in_merge() -> bool:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...