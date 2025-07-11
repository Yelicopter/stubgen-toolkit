import argparse
import enum
import logging
from collections.abc import Sequence
from flake8.plugins.finder import Plugins as Plugins
from typing import Any, Callable, Optional

LOG: logging.Logger

class Option:
    short_option_name: str | enum.Enum
    long_option_name: str | enum.Enum
    option_args: list[str]
    action: str | enum.Enum | type[argparse.Action]
    default: Any
    type_: Callable[..., Any] | enum.Enum
    dest: str | enum.Enum
    nargs: str | int | enum.Enum
    const: Any
    choices: Sequence[Any] | enum.Enum
    help: str | enum.Enum
    metavar: str | enum.Enum
    required: bool | enum.Enum
    option_kwargs: dict[str, Any]
    parse_from_config: bool
    comma_separated_list: bool
    normalize_paths: bool
    config_name: Optional[str]
    def __init__(self, short_option_name: str | enum.Enum = ..., long_option_name: str | enum.Enum = ..., action: str | enum.Enum | type[argparse.Action] = ..., default: Any = ..., type_: Callable[..., Any] | enum.Enum = ..., dest: str | enum.Enum = ..., nargs: str | int | enum.Enum = ..., const: Any = ..., choices: Sequence[Any] | enum.Enum = ..., help: str | enum.Enum = ..., metavar: str | enum.Enum = ..., required: bool | enum.Enum = ..., parse_from_config: bool = ..., comma_separated_list: bool = ..., normalize_paths: bool = ...) -> None: ...
    @property
    def filtered_option_kwargs(self) -> dict[str, Any]: ...
    def normalize(self, value: Any, *normalize_args: str) -> Any: ...
    def to_argparse(self) -> tuple[list[str], dict[str, Any]]: ...

class OptionManager:
    formatter_names: list[str]
    parser: argparse.ArgumentParser
    config_options_dict: dict[str, Option]
    options: list[Option]
    extended_default_ignore: list[str]
    extended_default_select: list[str]
    def __init__(self, *, version: str, plugin_versions: str, parents: list[argparse.ArgumentParser], formatter_names: list[str]) -> None: ...
    def register_plugins(self, plugins: Plugins) -> None: ...
    def add_option(self, *args: str, **kwargs: Any) -> None: ...
    def extend_default_ignore(self, error_codes: list[str]) -> None: ...
    def extend_default_select(self, error_codes: list[str]) -> None: ...
    def parse_args(self, args: Optional[Sequence[str]] = ..., values: Optional[argparse.Namespace] = ...) -> argparse.Namespace: ...
