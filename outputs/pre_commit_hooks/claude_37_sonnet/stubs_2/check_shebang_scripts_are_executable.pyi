"""Check that text files with a shebang are executable."""
from __future__ import annotations

import argparse
import shlex
import sys
from collections.abc import Sequence
from typing import List, Optional, Set

from pre_commit_hooks.check_executables_have_shebangs import EXECUTABLE_VALUES
from pre_commit_hooks.check_executables_have_shebangs import git_ls_files
from pre_commit_hooks.check_executables_have_shebangs import has_shebang


def check_shebangs(paths: List[str]) -> int: ...


def _check_git_filemode(paths: Sequence[str]) -> int: ...


def _message(path: str) -> None: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())