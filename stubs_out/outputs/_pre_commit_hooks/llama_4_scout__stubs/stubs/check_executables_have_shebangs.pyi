from collections.abc import Generator, Sequence
from pre_commit_hooks.util import cmd_output as cmd_output, zsplit as zsplit
from typing import NamedTuple

EXECUTABLE_VALUES: frozenset[str]

def check_executables(paths: Sequence[str]) -> int: ...

class GitLsFile(NamedTuple):
    mode: str
    filename: str

def git_ls_files(paths: Sequence[str]) -> Generator[GitLsFile, None, None]: ...
def has_shebang(path: str) -> bool: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
