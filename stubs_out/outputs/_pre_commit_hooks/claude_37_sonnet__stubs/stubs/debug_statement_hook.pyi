import ast
from _typeshed import Incomplete
from collections.abc import Sequence
from typing import NamedTuple

DEBUG_STATEMENTS: Incomplete

class Debug(NamedTuple):
    line: int
    col: int
    name: str
    reason: str

class DebugStatementParser(ast.NodeVisitor):
    breakpoints: Incomplete
    def __init__(self) -> None: ...
    def visit_Import(self, node: ast.Import) -> None: ...
    def visit_ImportFrom(self, node: ast.ImportFrom) -> None: ...
    def visit_Call(self, node: ast.Call) -> None: ...

def check_file(filename: str) -> int: ...
def main(argv: Sequence[str] = ...) -> int: ...
