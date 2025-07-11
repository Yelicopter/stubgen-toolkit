from __future__ import annotations

import argparse
import ast
import traceback
from collections.abc import Sequence
from typing import List, NamedTuple, Optional


DEBUG_STATEMENTS = {
    'bpdb',
    'ipdb',
    'pdb',
    'pdbr',
    'pudb',
    'pydevd_pycharm',
    'q',
    'rdb',
    'rpdb',
    'wdb',
}


class Debug(NamedTuple):
    line: int
    col: int
    name: str
    reason: str


class DebugStatementParser(ast.NodeVisitor):
    def __init__(self) -> None:
        self.breakpoints: List[Debug] = []

    def visit_Import(self, node: ast.Import) -> None: ...

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None: ...

    def visit_Call(self, node: ast.Call) -> None: ...


def check_file(filename: str) -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())