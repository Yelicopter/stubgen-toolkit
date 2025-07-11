from __future__ import annotations

import argparse
from collections.abc import Generator, Sequence
from typing import Any, Dict, List, NamedTuple, Optional, Union

import ruamel.yaml

yaml = ruamel.yaml.YAML(typ='safe')


def _exhaust(gen: Generator[Any, None, None]) -> None: ...


def _parse_unsafe(*args: Any, **kwargs: Any) -> None: ...


def _load_all(*args: Any, **kwargs: Any) -> None: ...


class Key(NamedTuple):
    multi: bool
    unsafe: bool


LOAD_FNS = {
    Key(multi=False, unsafe=False): yaml.load,
    Key(multi=False, unsafe=True): _parse_unsafe,
    Key(multi=True, unsafe=False): _load_all,
    Key(multi=True, unsafe=True): _parse_unsafe,
}


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())
