import ruamel.yaml
from collections.abc import Sequence
from typing import Any, Callable, Final, NamedTuple

yaml: Final[ruamel.yaml.YAML]

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: Final[dict[Key, Callable[..., Any]]]

def main(argv: Sequence[str] | None = ...) -> int: ...
