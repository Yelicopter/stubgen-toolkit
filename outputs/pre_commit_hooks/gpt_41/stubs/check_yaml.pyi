from typing import Sequence, Generator, Optional, Any, NamedTuple, Callable

import ruamel.yaml

def _exhaust(gen: Generator[Any, None, None]) -> None: ...
def _parse_unsafe(*args: Any, **kwargs: Any) -> None: ...
def _load_all(*args: Any, **kwargs: Any) -> None: ...

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: dict[Key, Callable[..., Any]]

def main(argv: Optional[Sequence[str]] = ...) -> int: ...