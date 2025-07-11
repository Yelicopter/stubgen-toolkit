"""Sort a simple YAML file, keeping blocks of comments and definitions
together.

We assume a strict subset of YAML that looks like:

    # block of header comments
    # here that should always
    # be at the top of the file

    # optional comments
    # can go here
    key: value
    key: value

    key: value

In other words, we don't sort deeper than the top layer, and might corrupt
complicated YAML files.
"""
from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import List, Optional


QUOTES = ["'", '"']


def sort(lines: List[str]) -> List[str]: ...


def parse_block(lines: List[str], header: bool = False) -> List[str]: ...


def parse_blocks(lines: List[str]) -> List[List[str]]: ...


def first_key(lines: List[str]) -> str: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())