from __future__ import annotations

from collections.abc import Sequence
from typing import Final

ORDINARY_CHANGED_ENTRIES_MARKER: Final[str]
PERMS_LINK: Final[str]
PERMS_NONEXIST: Final[str]

def find_destroyed_symlinks(files: list[str]) -> list[str]: ...
def main(argv: Sequence[str] | None = None) -> int: ...