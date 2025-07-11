from __future__ import annotations

import argparse
import enum
import functools
import logging
from collections.abc import Sequence
from typing import Any, Callable, Optional

from flake8 import utils
from flake8.plugins.finder import Plugins

LOG = logging.getLogger(__name__)


# represent a singleton of "not passed arguments".
# an enum is chosen to trick mypy
_ARG = enum.Enum("_ARG", "NO")


def _flake8_normalize(
    value: Any,
    *args: Any,
    comma_separated_list: bool = False,
    normalize_paths: bool = False,
) -> Any:
    ...


class Option:
    def __init__(
        self,
        short_option_name: str = _ARG.NO,
        long_option_name: str = _ARG.NO,
        action: str = _ARG.NO,
        default: Any = _ARG.NO,
        type: Callable[[Any], Any] = _ARG.NO,
        dest: str = _ARG.NO,
        nargs: Any = _ARG.NO,
        const: Any = _ARG.NO,
        choices: Any = _ARG.NO,
        help: Any = _ARG.NO,
        metavar: Any = _ARG.NO,
        required: bool = _ARG.NO,
        parse_from_config: bool = False,
        comma_separated_list: bool = False,
        normalize_paths: bool = False,
    ) -> None:
        ...

    @property
    def filtered_option_kwargs(self) -> dict:
        ...

    def __repr__(self) -> str:
        ...

    def normalize(self, value: Any, *normalize_args: Any) -> Any:
        ...

    def to_argparse(self) -> Any:
        ...


class OptionManager:
    def __init__(
        self,
        *,
        version: str,
        plugin_versions: str,
        parents: Sequence[argparse.ArgumentParser],
        formatter_names: Sequence[str],
    ) -> None:
        ...

    def register_plugins(self, plugins: Plugins) -> None:
        ...

    def add_option(self, *args: Any, **kwargs: Any) -> None:
        ...

    def extend_default_ignore(self, error_codes: Sequence[str]) -> None:
        ...

    def extend_default_select(self, error_codes: Sequence[str]) -> None:
        ...

    def parse_args(
        self,
        args: Optional[Sequence[str]] = None,
        values: Optional[argparse.Namespace] = None,
    ) -> argparse.Namespace:
        ...