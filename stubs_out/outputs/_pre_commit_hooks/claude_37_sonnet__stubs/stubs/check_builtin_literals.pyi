import ast
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import List, NamedTuple, Optional, Set

BUILTIN_TYPES: Incomplete

class Call(NamedTuple):
    name: str
    line: int
    column: int

class Visitor(ast.NodeVisitor):
    builtin_type_calls: Incomplete
    ignore: Incomplete
    allow_dict_kwargs: Incomplete
    def __init__(self, ignore: Optional[Sequence[str]] = ..., allow_dict_kwargs: bool = ...) -> None: ...
    def visit_Call(self, node: ast.Call) -> None: ...

def check_file(filename: str, ignore: Optional[Sequence[str]] = ..., allow_dict_kwargs: bool = ...) -> List[Call]: ...
def parse_ignore(value: str) -> Set[str]: ...
def main(argv: Sequence[str] = ...) -> int: ...
