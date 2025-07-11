from _typeshed import Incomplete
from collections.abc import Generator, Sequence
from pre_commit_hooks.util import cmd_output as cmd_output, zsplit as zsplit
from typing import List, NamedTuple, Optional

EXECUTABLE_VALUES: Incomplete

def check_executables(paths: List[str]) -> int: ...

class GitLsFile(NamedTuple):
    mode: str
    filename: str

def git_ls_files(paths: Sequence[str]) -> Generator[GitLsFile, None, None]: ...
def has_shebang(path: str) -> bool: ...
def main(argv: Optional[Sequence[str]] = ...) -> int: ...
