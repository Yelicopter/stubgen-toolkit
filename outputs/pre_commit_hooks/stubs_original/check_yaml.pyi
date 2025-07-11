from _typeshed import Incomplete as Incomplete
from collections.abc import Sequence
from typing import NamedTuple

yaml: Incomplete

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: Incomplete

def main(argv: Sequence[str] | None = ...) -> int: ...
