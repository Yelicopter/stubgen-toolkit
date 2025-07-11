from collections.abc import Sequence
from pre_commit_hooks.util import cmd_output as cmd_output, zsplit as zsplit

ORDINARY_CHANGED_ENTRIES_MARKER: str
PERMS_LINK: str
PERMS_NONEXIST: str

def find_destroyed_symlinks(files: Sequence[str]) -> list[str]: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
