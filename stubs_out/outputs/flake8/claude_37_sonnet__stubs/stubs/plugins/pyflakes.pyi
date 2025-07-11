import argparse
import ast
import logging
import pyflakes.checker
from collections.abc import Generator
from flake8.options.manager import OptionManager as OptionManager
from typing import Dict, Tuple, Type

LOG: logging.Logger
FLAKE8_PYFLAKES_CODES: Dict[str, str]

class FlakesChecker(pyflakes.checker.Checker):
    with_doctest: bool
    builtIns: set[str]
    def __init__(self, tree: ast.AST, filename: str) -> None: ...
    @classmethod
    def add_options(cls, parser: OptionManager) -> None: ...
    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None: ...
    def run(self) -> Generator[Tuple[int, int, str, Type], None, None]: ...
