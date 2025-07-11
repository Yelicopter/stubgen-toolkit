import pyflakes.checker
from _typeshed import Incomplete
from collections.abc import Generator
from flake8.options.manager import OptionManager as OptionManager
from typing import Any

LOG: Incomplete
FLAKE8_PYFLAKES_CODES: Incomplete

class FlakesChecker(pyflakes.checker.Checker):
    with_doctest: bool
    def __init__(self, tree: Any, filename: str) -> None: ...
    @classmethod
    def add_options(cls, parser: OptionManager) -> None: ...
    @classmethod
    def parse_options(cls, options: Any) -> None: ...
    def run(self) -> Generator: ...
