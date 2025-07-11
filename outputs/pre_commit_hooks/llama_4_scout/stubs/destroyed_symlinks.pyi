from __future__ import annotations

import argparse
import shlex
import subprocess
from collections.abc import Sequence

from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import zsplit

ORDINARY_CHANGED_ENTRIES_MARKER: str = ''
PERMS_LINK: str = ''
PERMS_NONEXIST: str = ''

def find_destroyed_symlinks(files: Sequence[str]) -> list[str]:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...