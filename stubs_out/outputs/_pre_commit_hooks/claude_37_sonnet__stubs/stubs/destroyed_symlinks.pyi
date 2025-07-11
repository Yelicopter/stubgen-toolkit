from collections.abc import Sequence
from typing import List

ORDINARY_CHANGED_ENTRIES_MARKER: str
PERMS_LINK: str
PERMS_NONEXIST: str

def find_destroyed_symlinks(files: Sequence[str]) -> List[str]: ...
def main(argv: Sequence[str] = ...) -> int: ...
