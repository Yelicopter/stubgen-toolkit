import inspect
import os
import platform
import shutil
import subprocess
import sys
import traceback
from datetime import datetime
from enum import Enum
from functools import update_wrapper
from pathlib import Path
from traceback import FrameSummary, StackSummary
from types import TracebackType
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Type, Union
from uuid import UUID

import click
from typer._types import TyperChoice

from typing import get_args, get_origin, Union as _Union
from .completion import get_completion_inspect_parameters
from .core import (
    DEFAULT_MARKUP_MODE,
    MarkupMode,
    TyperArgument,
    TyperCommand,
    TyperGroup,
    TyperOption,
)
from .models import (
    AnyType,
    ArgumentInfo,
    CommandFunctionType,
    CommandInfo,
    Default,
    DefaultPlaceholder,
    DeveloperExceptionConfig,
    FileBinaryRead,
    FileBinaryWrite,
    FileText,
    FileTextWrite,
    NoneType,
    OptionInfo,
    ParameterInfo,
    ParamMeta,
    Required,
    TyperInfo,
    TyperPath,
)
from .utils import get_params_from_function

_original_except_hook: Callable[[Type[BaseException], BaseException, Optional[TracebackType]], None]
_typer_developer_exception_attr_name: str

def is_union(tp: Any) -> bool: ...
def except_hook(
    exc_type: Type[BaseException], exc_value: BaseException, tb: Optional[TracebackType]
) -> None: ...
def get_install_completion_arguments() -> Tuple[click.Parameter, click.Parameter]: ...

class Typer:
    _add_completion: bool
    rich_markup_mode: MarkupMode
    rich_help_panel: Optional[str]
    pretty_exceptions_enable: bool
    pretty_exceptions_show_locals: bool
    pretty_exceptions_short: bool
    info: TyperInfo
    registered_groups: List[TyperInfo]
    registered_commands: List[CommandInfo]
    registered_callback: Optional[TyperInfo]

    def __init__(
        self,
        *,
        name: Any = Default(None),
        cls: Any = Default(None),
        invoke_without_command: bool = Default(False),
        no_args_is_help: bool = Default(False),
        subcommand_metavar: Optional[str] = Default(None),
        chain: bool = Default(False),
        result_callback: Optional[Callable[..., Any]] = Default(None),
        context_settings: Optional[Dict[str, Any]] = Default(None),
        callback: Optional[Callable[..., Any]] = Default(None),
        help: Optional[str] = Default(None),
        epilog: Optional[str] = Default(None),
        short_help: Optional[str] = Default(None),
        options_metavar: str = Default("[OPTIONS]"),
        add_help_option: bool = Default(True),
        hidden: bool = Default(False),
        deprecated: bool = Default(False),
        add_completion: bool = True,
        rich_markup_mode: MarkupMode = Default(DEFAULT_MARKUP_MODE),
        rich_help_panel: Optional[str] = Default(None),
        pretty_exceptions_enable: bool = True,
        pretty_exceptions_show_locals: bool = True,
        pretty_exceptions_short: bool = True,
    ) -> None: ...
    def callback(
        self,
        *,
        cls: Any = Default(None),
        invoke_without_command: bool = Default(False),
        no_args_is_help: bool = Default(False),
        subcommand_metavar: Optional[str] = Default(None),
        chain: bool = Default(False),
        result_callback: Optional[Callable[..., Any]] = Default(None),
        context_settings: Optional[Dict[str, Any]] = Default(None),
        help: Optional[str] = Default(None),
        epilog: Optional[str] = Default(None),
        short_help: Optional[str] = Default(None),
        options_metavar: str = Default("[OPTIONS]"),
        add_help_option: bool = Default(True),
        hidden: bool = Default(False),
        deprecated: bool = Default(False),
        rich_help_panel: Optional[str] = Default(None),
    ) -> Callable[[CommandFunctionType], CommandFunctionType]: ...
    def command(
        self,
        name: Optional[str] = None,
        *,
        cls: Optional[Type[TyperCommand]] = None,
        context_settings: Optional[Dict[str, Any]] = None,
        help: Optional[str] = None,
        epilog: Optional[str] = None,
        short_help: Optional[str] = None,
        options_metavar: str = "[OPTIONS]",
        add_help_option: bool = True,
        no_args_is_help: bool = False,
        hidden: bool = False,
        deprecated: bool = False,
        rich_help_panel: Optional[str] = Default(None),
    ) -> Callable[[CommandFunctionType], CommandFunctionType]: ...
    def add_typer(
        self,
        typer_instance: "Typer",
        *,
        name: Optional[str] = Default(None),
        cls: Any = Default(None),
        invoke_without_command: bool = Default(False),
        no_args_is_help: bool = Default(False),
        subcommand_metavar: Optional[str] = Default(None),
        chain: bool = Default(False),
        result_callback: Optional[Callable[..., Any]] = Default(None),
        context_settings: Optional[Dict[str, Any]] = Default(None),
        callback: Optional[Callable[..., Any]] = Default(None),
        help: Optional[str] = Default(None),
        epilog: Optional[str] = Default(None),
        short_help: Optional[str] = Default(None),
        options_metavar: str = Default("[OPTIONS]"),
        add_help_option: bool = Default(True),
        hidden: bool = Default(False),
        deprecated: bool = Default(False),
        rich_help_panel: Optional[str] = Default(None),
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

def get_group(typer_instance: Typer) -> TyperGroup: ...
def get_command(typer_instance: Typer) -> Union[TyperCommand, TyperGroup]: ...
def solve_typer_info_help(typer_info: TyperInfo) -> str: ...
def solve_typer_info_defaults(typer_info: TyperInfo) -> TyperInfo: ...
def get_group_from_info(
    group_info: TyperInfo,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: MarkupMode,
) -> TyperGroup: ...
def get_command_name(name: str) -> str: ...
def get_params_convertors_ctx_param_name_from_function(
    callback: Optional[Callable[..., Any]],
) -> Tuple[List[click.Parameter], Dict[str, Callable[[Any], Any]], Optional[str]]: ...
def get_command_from_info(
    command_info: CommandInfo,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: MarkupMode,
) -> TyperCommand: ...
def determine_type_convertor(type_: Any) -> Optional[Callable[[Any], Any]]: ...
def param_path_convertor(value: Optional[str] = None) -> Optional[Path]: ...
def generate_enum_convertor(enum: Type[Enum]) -> Callable[[Optional[str]], Optional[Enum]]: ...
def generate_list_convertor(
    convertor: Optional[Callable[[Any], Any]], default_value: Optional[List[Any]]
) -> Callable[[Optional[List[Any]]], Optional[List[Any]]]: ...
def generate_tuple_convertor(
    types: List[Any],
) -> Callable[[Optional[Tuple[Any, ...]], ], Optional[Tuple[Any, ...]]]: ...
def get_callback(
    *,
    callback: Optional[Callable[..., Any]] = None,
    params: List[click.Parameter] = [],
    convertors: Optional[Dict[str, Callable[[Any], Any]]] = None,
    context_param_name: Optional[str] = None,
    pretty_exceptions_short: bool,
) -> Optional[Callable[..., Any]]: ...
def get_click_type(
    *, annotation: Any, parameter_info: ParameterInfo
) -> click.types.ParamType: ...
def lenient_issubclass(
    cls: Any, class_or_tuple: Union[Type[Any], Tuple[Type[Any], ...]]
) -> bool: ...
def get_click_param(
    param: ParamMeta,
) -> Tuple[click.Parameter, Optional[Callable[[Any], Any]]]: ...
def run(function: CommandFunctionType) -> None: ...
def _is_macos() -> bool: ...
def _is_linux_or_bsd() -> bool: ...
def launch(url: str, wait: bool = False, locate: bool = False) -> int: ...