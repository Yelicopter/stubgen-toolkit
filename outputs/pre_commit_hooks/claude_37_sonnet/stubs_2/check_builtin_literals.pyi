from __future__ import annotations

import argparse
import ast
from collections.abc import Sequence
from typing import List, NamedTuple, Optional, Set


BUILTIN_TYPES = {
    'complex': '0j',
    'dict': '{}',
    'float': '0.0',
    'int': '0',
    'list': '[]',
    'str': "''",
    'tuple': '()',
}


class Call(NamedTuple):
    name: str
    line: int
    column: int


class Visitor(ast.NodeVisitor):
    def __init__(
            self,
            ignore: Optional[Sequence[str]] = None,
            allow_dict_kwargs: bool = True,
    ) -> None:
        self.builtin_type_calls: List[Call] = []
        self.ignore = set(ignore) if ignore else set()
        self.allow_dict_kwargs = allow_dict_kwargs

    def _check_dict_call(self, node: ast.Call) -> bool: ...

    def visit_Call(self, node: ast.Call) -> None: ...


def check_file(
        filename: str,
        ignore: Optional[Sequence[str]] = None,
        allow_dict_kwargs: bool = True,
) -> List[Call]: ...


def parse_ignore(value: str) -> Set[str]: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())