from __future__ import annotations

import argparse
import shlex
import sys
from collections.abc import Generator
from collections.abc import Sequence
from typing import NamedTuple

from pre_commit_hooks.util import cmd_output
from pre_commit_hooks.util import zsplit

EXECUTABLE_VALUES: frozenset[str] = frozenset()

def check_executables(paths: Sequence[str]) -> int:
    ...

class GitLsFile(NamedTuple):
    mode: str
    filename: str

def git_ls_files(paths: Sequence[str]) -> Generator[GitLsFile, None, None]:
    ...

def _check_git_filemode(paths: Sequence[str]) -> int:
    ...

def has_shebang(path: str) -> bool:
    ...

def _message(path: str) -> None:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...