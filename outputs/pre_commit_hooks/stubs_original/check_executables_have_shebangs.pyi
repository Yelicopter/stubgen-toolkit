from _typeshed import Incomplete as Incomplete
from collections.abc import Generator, Sequence
from typing import NamedTuple

EXECUTABLE_VALUES: Incomplete

def check_executables(paths: list[str]) -> int: ...

class GitLsFile(NamedTuple):
    mode: str
    filename: str

def git_ls_files(paths: Sequence[str]) -> Generator[GitLsFile]: ...
def has_shebang(path: str) -> int: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
