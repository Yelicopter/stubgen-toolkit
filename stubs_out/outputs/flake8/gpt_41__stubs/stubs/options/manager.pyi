import argparse
import enum
from collections.abc import Sequence
from flake8.plugins.finder import Plugins as Plugins
from typing import Any

class Option:
    short_option_name: str | enum.Enum
    long_option_name: str | enum.Enum
    option_args: list[str | enum.Enum]
    action: Any
    default: Any
    type: Any
    dest: Any
    nargs: Any
    const: Any
    choices: Any
    help: Any
    metavar: Any
    required: Any
    option_kwargs: dict[str, Any]
    parse_from_config: bool
    comma_separated_list: bool
    normalize_paths: bool
    config_name: str | None
    def __init__(self, short_option_name: str | enum.Enum = ..., long_option_name: str | enum.Enum = ..., action: Any = ..., default: Any = ..., type: Any = ..., dest: Any = ..., nargs: Any = ..., const: Any = ..., choices: Any = ..., help: Any = ..., metavar: Any = ..., required: Any = ..., parse_from_config: bool = ..., comma_separated_list: bool = ..., normalize_paths: bool = ...) -> None: ...
    @property
    def filtered_option_kwargs(self) -> dict[str, Any]: ...
    def normalize(self, value: Any, *normalize_args: Any) -> Any: ...
    def to_argparse(self) -> tuple[list[str | enum.Enum], dict[str, Any]]: ...

class OptionManager:
    formatter_names: list[str]
    parser: argparse.ArgumentParser
    config_options_dict: dict[str, Option]
    options: list[Option]
    extended_default_ignore: list[str]
    extended_default_select: list[str]
    def __init__(self, *, version: str, plugin_versions: str, parents: Sequence[argparse.ArgumentParser], formatter_names: list[str]) -> None: ...
    def register_plugins(self, plugins: Plugins) -> None: ...
    def add_option(self, *args: Any, **kwargs: Any) -> None: ...
    def extend_default_ignore(self, error_codes: list[str]) -> None: ...
    def extend_default_select(self, error_codes: list[str]) -> None: ...
    def parse_args(self, args: Sequence[str] | None = ..., values: argparse.Namespace | None = ...) -> argparse.Namespace: ...
