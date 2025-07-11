from __future__ import annotations

import argparse
from collections.abc import Sequence

ORDINARY_CHANGED_ENTRIES_MARKER: str
PERMS_LINK: str
PERMS_NONEXIST: str

def find_destroyed_symlinks(files: Sequence[str]) -> list[str]: ...

def main(argv: Sequence[str] | None = None) -> int: ...