import ast
from _typeshed import Incomplete as Incomplete
from collections.abc import Sequence
from typing import NamedTuple

BUILTIN_TYPES: Incomplete

class Call(NamedTuple):
    name: str
    line: int
    column: int

class Visitor(ast.NodeVisitor):
    builtin_type_calls: Incomplete
    ignore: Incomplete
    allow_dict_kwargs: Incomplete
    def __init__(self, ignore: Sequence[str] | None = ..., allow_dict_kwargs: bool = ...) -> None: ...
    def visit_Call(self, node: ast.Call) -> None: ...

def check_file(filename: str, ignore: Sequence[str] | None = ..., allow_dict_kwargs: bool = ...) -> list[Call]: ...
def parse_ignore(value: str) -> set[str]: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
