import ruamel.yaml
from collections.abc import Sequence
from typing import Any, NamedTuple

yaml: ruamel.yaml.YAML

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: dict[Key, Any]

def main(argv: Sequence[str] | None = ...) -> int: ...
