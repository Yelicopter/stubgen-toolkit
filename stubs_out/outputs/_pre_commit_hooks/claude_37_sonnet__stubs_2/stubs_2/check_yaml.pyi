from _typeshed import Incomplete
from collections.abc import Sequence
from typing import NamedTuple, Optional

yaml: Incomplete

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: Incomplete

def main(argv: Optional[Sequence[str]] = ...) -> int: ...
