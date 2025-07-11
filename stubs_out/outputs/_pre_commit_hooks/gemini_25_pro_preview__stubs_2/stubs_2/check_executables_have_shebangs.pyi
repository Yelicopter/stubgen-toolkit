from collections.abc import Generator, Sequence
from typing import Final, NamedTuple

EXECUTABLE_VALUES: Final[frozenset[str]]

def check_executables(paths: list[str]) -> int: ...

class GitLsFile(NamedTuple):
    mode: str
    filename: str

def git_ls_files(paths: list[str]) -> Generator[GitLsFile, None, None]: ...
def has_shebang(path: str) -> bool: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
