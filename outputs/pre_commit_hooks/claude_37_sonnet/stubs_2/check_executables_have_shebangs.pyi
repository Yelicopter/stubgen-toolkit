"""Check that executable text files have a shebang."""
from __future__ import annotations

import argparse
import shlex
import sys
from collections.abc import Generator, Sequence
from typing import List, NamedTuple, Optional, Set

from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import zsplit

EXECUTABLE_VALUES = frozenset(('1', '3', '5', '7'))


def check_executables(paths: List[str]) -> int: ...


class GitLsFile(NamedTuple):
    mode: str
    filename: str


def git_ls_files(paths: Sequence[str]) -> Generator[GitLsFile, None, None]: ...


def _check_git_filemode(paths: Sequence[str]) -> int: ...


def has_shebang(path: str) -> bool: ...


def _message(path: str) -> None: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())