import ast
from collections.abc import Sequence
from typing import NamedTuple

BUILTIN_TYPES: dict[str, str]

class Call(NamedTuple):
    name: str
    line: int
    column: int

class Visitor(ast.NodeVisitor):
    def __init__(self, ignore: Sequence[str] | None = ..., allow_dict_kwargs: bool = ...) -> None: ...
    def visit_Call(self, node: ast.Call) -> None: ...

def check_file(filename: str, ignore: Sequence[str] | None = ..., allow_dict_kwargs: bool = ...) -> Sequence[Call]: ...
def parse_ignore(value: str) -> set[str]: ...
def main(argv: Sequence[str] | None = ...) -> int: ...
