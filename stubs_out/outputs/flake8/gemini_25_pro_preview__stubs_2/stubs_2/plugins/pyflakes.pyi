import argparse
import ast
import logging
import pyflakes.checker
from collections.abc import Generator
from flake8.options.manager import OptionManager as OptionManager
from typing import Type

LOG: logging.Logger
FLAKE8_PYFLAKES_CODES: dict[str, str]

class FlakesChecker(pyflakes.checker.Checker):
    with_doctest: bool
    def __init__(self, tree: ast.AST, filename: str) -> None: ...
    @classmethod
    def add_options(cls, parser: OptionManager) -> None: ...
    @classmethod
    def parse_options(cls, options: argparse.Namespace) -> None: ...
    def run(self) -> Generator[tuple[int, int, str, Type[pyflakes.messages.Message]], None, None]: ...
