import argparse
import enum
import logging
from collections.abc import Sequence
from flake8 import utils as utils
from flake8.plugins.finder import Plugins as Plugins
from typing import Any, Dict, List, Optional, Tuple, Union

LOG: logging.Logger

class _ARG(enum.Enum):
    NO: Any

class Option:
    short_option_name: Union[str, _ARG]
    long_option_name: Union[str, _ARG]
    option_args: list[str]
    action: Union[str, _ARG]
    default: Any
    type: Any
    dest: Union[str, _ARG]
    nargs: Union[str, int, _ARG]
    const: Any
    choices: Any
    help: Union[str, _ARG]
    metavar: Union[str, _ARG]
    required: Union[bool, _ARG]
    option_kwargs: Dict[str, Any]
    parse_from_config: bool
    comma_separated_list: bool
    normalize_paths: bool
    config_name: Optional[str]
    def __init__(self, short_option_name: Union[str, _ARG] = ..., long_option_name: Union[str, _ARG] = ..., action: Union[str, _ARG] = ..., default: Any = ..., type: Any = ..., dest: Union[str, _ARG] = ..., nargs: Union[str, int, _ARG] = ..., const: Any = ..., choices: Any = ..., help: Union[str, _ARG] = ..., metavar: Union[str, _ARG] = ..., required: Union[bool, _ARG] = ..., parse_from_config: bool = ..., comma_separated_list: bool = ..., normalize_paths: bool = ...) -> None: ...
    @property
    def filtered_option_kwargs(self) -> Dict[str, Any]: ...
    def normalize(self, value: Any, *normalize_args: Any) -> Any: ...
    def to_argparse(self) -> Tuple[List[str], Dict[str, Any]]: ...

class OptionManager:
    formatter_names: list[str]
    parser: argparse.ArgumentParser
    config_options_dict: Dict[str, Option]
    options: list[Option]
    extended_default_ignore: list[str]
    extended_default_select: list[str]
    def __init__(self, *, version: str, plugin_versions: str, parents: list[argparse.ArgumentParser], formatter_names: list[str]) -> None: ...
    def register_plugins(self, plugins: Plugins) -> None: ...
    def add_option(self, *args: Any, **kwargs: Any) -> None: ...
    def extend_default_ignore(self, error_codes: Sequence[str]) -> None: ...
    def extend_default_select(self, error_codes: Sequence[str]) -> None: ...
    def parse_args(self, args: Optional[Sequence[str]] = ..., values: Optional[argparse.Namespace] = ...) -> argparse.Namespace: ...
