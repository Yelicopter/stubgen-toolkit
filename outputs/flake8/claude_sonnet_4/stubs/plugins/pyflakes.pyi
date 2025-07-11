import argparse
import ast
import logging
from collections.abc import Generator
from typing import Any
import pyflakes.checker
from flake8.options.manager import OptionManager

LOG: ...
FLAKE8_PYFLAKES_CODES: dict[str, str]

class FlakesChecker(pyflakes.checker.Checker):
    with_doctest: bool
    
    def __init__(self, tree: ast.AST, filename: str) -> None: ...
    @classmethod
    def add_options(cls, parser: OptionManager) -> None: ...
    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None: ...
    def run(self) -> Generator[tuple[int, int, str, type], None, None]: ...