from __future__ import annotations

import argparse
import ast
from collections.abc import Sequence
from typing import NamedTuple

BUILTIN_TYPES: dict[str, str]

class Call(NamedTuple):
    name: str
    line: int
    column: int

class Visitor(ast.NodeVisitor):
    builtin_type_calls: list[Call]
    ignore: set[str]
    allow_dict_kwargs: bool
    
    def __init__(
        self,
        ignore: Sequence[str] | None = None,
        allow_dict_kwargs: bool = True,
    ) -> None: ...
    
    def _check_dict_call(self, node: ast.Call) -> bool: ...
    def visit_Call(self, node: ast.Call) -> None: ...

def check_file(
    filename: str,
    ignore: Sequence[str] | None = None,
    allow_dict_kwargs: bool = True,
) -> list[Call]: ...

def parse_ignore(value: str) -> set[str]: ...

def main(argv: Sequence[str] | None = None) -> int: ...