import argparse
import ast
import logging
from collections.abc import Generator
from typing import Any
from flake8.options.manager import OptionManager

FLAKE8_PYFLAKES_CODES: dict[str, str]
LOG: logging.Logger

class FlakesChecker:
    with_doctest: bool
    builtIns: set[str]
    def __init__(self, tree: ast.AST, filename: str) -> None: ...
    @classmethod
    def add_options(cls, parser: OptionManager) -> None: ...
    @classmethod
    def parse_options(cls, options: Any) -> None: ...
    def run(self) -> Generator[tuple[int, int, str, type], None, None]: ...