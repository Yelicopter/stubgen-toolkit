from typing import Any, Callable, NamedTuple, Optional, Sequence

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: dict[Key, Callable[..., Any]]

def main(argv: Optional[Sequence[str]] = ...) -> int: ...
