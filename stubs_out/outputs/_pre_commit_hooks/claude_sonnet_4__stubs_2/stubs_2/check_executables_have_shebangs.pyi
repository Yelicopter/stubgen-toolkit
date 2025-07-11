from collections.abc import Generator, Sequence
from typing import NamedTuple

EXECUTABLE_VALUES: frozenset[str]

def check_executables(paths: Sequence[str]) -> int: ...

class GitLsFile(NamedTuple):
    mode: str
    filename: str

def git_ls_files(paths: Sequence[str]) -> Generator[GitLsFile, None, None]: ...
def has_shebang(path: str) -> bool: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
