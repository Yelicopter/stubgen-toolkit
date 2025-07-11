from collections.abc import Sequence
from pre_commit_hooks.util import cmd_output as cmd_output, zsplit as zsplit
from typing import List, Optional

ORDINARY_CHANGED_ENTRIES_MARKER: str
PERMS_LINK: str
PERMS_NONEXIST: str

def find_destroyed_symlinks(files: Sequence[str]) -> List[str]: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...
