from __future__ import annotations

import argparse
import enum
import functools
import logging
from collections.abc import Sequence
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from flake8 import utils
from flake8.plugins.finder import Plugins

LOG: logging.Logger

_ARG: enum.Enum

def _flake8_normalize(
    value: Any,
    *args: Any,
    comma_separated_list: bool = False,
    normalize_paths: bool = False,
) -> Union[str, List[str]]: ...

class Option:
    short_option_name: Union[str, enum.Enum]
    long_option_name: Union[str, enum.Enum]
    option_args: list[str]
    action: Union[str, enum.Enum]
    default: Any
    type: Any
    dest: Union[str, enum.Enum]
    nargs: Union[str, int, enum.Enum]
    const: Any
    choices: Any
    help: Union[str, enum.Enum]
    metavar: Union[str, enum.Enum]
    required: Union[bool, enum.Enum]
    option_kwargs: Dict[str, Any]
    parse_from_config: bool
    comma_separated_list: bool
    normalize_paths: bool
    config_name: Optional[str]
    _opt: Optional[Any]

    def __init__(
        self,
        short_option_name: Union[str, enum.Enum] = _ARG.NO,
        long_option_name: Union[str, enum.Enum] = _ARG.NO,
        action: Union[str, enum.Enum] = _ARG.NO,
        default: Any = _ARG.NO,
        type: Any = _ARG.NO,
        dest: Union[str, enum.Enum] = _ARG.NO,
        nargs: Union[str, int, enum.Enum] = _ARG.NO,
        const: Any = _ARG.NO,
        choices: Any = _ARG.NO,
        help: Union[str, enum.Enum] = _ARG.NO,
        metavar: Union[str, enum.Enum] = _ARG.NO,
        required: Union[bool, enum.Enum] = _ARG.NO,
        parse_from_config: bool = False,
        comma_separated_list: bool = False,
        normalize_paths: bool = False,
    ) -> None: ...
    @property
    def filtered_option_kwargs(self) -> Dict[str, Any]: ...
    def __repr__(self) -> str: ...
    def normalize(self, value: Any, *normalize_args: Any) -> Any: ...
    def to_argparse(self) -> Tuple[List[str], Dict[str, Any]]: ...

class OptionManager:
    formatter_names: list[str]
    parser: argparse.ArgumentParser
    config_options_dict: Dict[str, Option]
    options: list[Option]
    extended_default_ignore: list[str]
    extended_default_select: list[str]
    _current_group: Optional[argparse._ArgumentGroup]

    def __init__(
        self,
        *,
        version: str,
        plugin_versions: str,
        parents: list[argparse.ArgumentParser],
        formatter_names: list[str],
    ) -> None: ...
    def register_plugins(self, plugins: Plugins) -> None: ...
    def add_option(self, *args: Any, **kwargs: Any) -> None: ...
    def extend_default_ignore(self, error_codes: Sequence[str]) -> None: ...
    def extend_default_select(self, error_codes: Sequence[str]) -> None: ...
    def parse_args(
        self,
        args: Optional[Sequence[str]] = None,
        values: Optional[argparse.Namespace] = None,
    ) -> argparse.Namespace: ...