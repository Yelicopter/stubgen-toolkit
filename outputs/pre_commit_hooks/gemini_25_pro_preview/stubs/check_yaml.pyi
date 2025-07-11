from __future__ import annotations

from collections.abc import Generator, Sequence
from typing import Any, Callable, Final, NamedTuple

import ruamel.yaml

yaml: Final[ruamel.yaml.YAML]

def _exhaust(gen: Generator[Any, None, None]) -> None: ...
def _parse_unsafe(*args: Any, **kwargs: Any) -> None: ...
def _load_all(*args: Any, **kwargs: Any) -> None: ...

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: Final[dict[Key, Callable[..., Any]]]

def main(argv: Sequence[str] | None = None) -> int: ...