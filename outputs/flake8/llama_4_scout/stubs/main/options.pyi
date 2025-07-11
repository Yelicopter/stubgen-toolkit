from __future__ import annotations

import argparse

from flake8 import defaults
from flake8.options.manager import OptionManager


def stage1_arg_parser() -> argparse.ArgumentParser:
    ...


class JobsArgument:
    def __init__(self, arg: str) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


def register_default_options(option_manager: OptionManager) -> None:
    ...