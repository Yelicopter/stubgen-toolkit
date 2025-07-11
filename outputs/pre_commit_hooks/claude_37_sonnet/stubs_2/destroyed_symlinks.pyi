from __future__ import annotations

import argparse
import shlex
import subprocess
from collections.abc import Sequence
from typing import List, Optional

from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import zsplit

ORDINARY_CHANGED_ENTRIES_MARKER = '1'
PERMS_LINK = '120000'
PERMS_NONEXIST = '000000'


def find_destroyed_symlinks(files: Sequence[str]) -> List[str]: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())