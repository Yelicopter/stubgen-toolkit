from __future__ import annotations

import argparse
from collections.abc import Generator
from collections.abc import Sequence
from typing import Any
from typing import NamedTuple

import ruamel.yaml

yaml: ruamel.yaml.YAML = ...

def _exhaust(gen: Generator[Any, None, None]) -> None:
    ...

def _parse_unsafe(*args: Any, **kwargs: Any) -> None:
    ...

def _load_all(*args: Any, **kwargs: Any) -> None:
    ...

class Key(NamedTuple):
    multi: bool
    unsafe: bool

LOAD_FNS: dict[Key, Any] = {}

def main(argv: Sequence[str] | None = None) -> int:
    ...