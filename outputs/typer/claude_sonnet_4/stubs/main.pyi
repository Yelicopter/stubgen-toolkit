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
from ._typing import get_args, get_origin, is_union
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

try:
    import rich
    from rich.traceback import Traceback
    from . import rich_utils
    console_stderr: Any
except ImportError:
    rich = None

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
        name: Union[str, DefaultPlaceholder] = ...,
        cls: Union[Type[TyperGroup], DefaultPlaceholder] = ...,
        invoke_without_command: Union[bool, DefaultPlaceholder] = ...,
        no_args_is_help: Union[bool, DefaultPlaceholder] = ...,
        subcommand_metavar: Union[str, DefaultPlaceholder] = ...,
        chain: Union[bool, DefaultPlaceholder] = ...,
        result_callback: Union[Callable[..., Any], DefaultPlaceholder] = ...,
        context_settings: Union[Dict[str, Any], DefaultPlaceholder] = ...,
        callback: Union[Callable[..., Any], DefaultPlaceholder] = ...,
        help: Union[str, DefaultPlaceholder] = ...,
        epilog: Union[str, DefaultPlaceholder] = ...,
        short_help: Union[str, DefaultPlaceholder] = ...,
        options_metavar: Union[str, DefaultPlaceholder] = ...,
        add_help_option: Union[bool, DefaultPlaceholder] = ...,
        hidden: Union[bool, DefaultPlaceholder] = ...,
        deprecated: Union[bool, DefaultPlaceholder] = ...,
        add_completion: bool = True,
        rich_markup_mode: Union[MarkupMode, DefaultPlaceholder] = ...,
        rich_help_panel: Union[str, DefaultPlaceholder] = ...,
        pretty_exceptions_enable: bool = True,
        pretty_exceptions_show_locals: bool = True,
        pretty_exceptions_short: bool = True,
    ) -> None: ...
    
    def callback(
        self,
        *,
        cls: Union[Type[TyperGroup], DefaultPlaceholder] = ...,
        invoke_without_command: Union[bool, DefaultPlaceholder] = ...,
        no_args_is_help: Union[bool, DefaultPlaceholder] = ...,
        subcommand_metavar: Union[str, DefaultPlaceholder] = ...,
        chain: Union[bool, DefaultPlaceholder] = ...,
        result_callback: Union[Callable[..., Any], DefaultPlaceholder] = ...,
        context_settings: Union[Dict[str, Any], DefaultPlaceholder] = ...,
        help: Union[str, DefaultPlaceholder] = ...,
        epilog: Union[str, DefaultPlaceholder] = ...,
        short_help: Union[str, DefaultPlaceholder] = ...,
        options_metavar: Union[str, DefaultPlaceholder] = ...,
        add_help_option: Union[bool, DefaultPlaceholder] = ...,
        hidden: Union[bool, DefaultPlaceholder] = ...,
        deprecated: Union[bool, DefaultPlaceholder] = ...,
        rich_help_panel: Union[str, DefaultPlaceholder] = ...,
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
        rich_help_panel: Union[str, DefaultPlaceholder] = ...,
    ) -> Callable[[CommandFunctionType], CommandFunctionType]: ...
    
    def add_typer(
        self,
        typer_instance: "Typer",
        *,
        name: Union[str, DefaultPlaceholder] = ...,
        cls: Union[Type[TyperGroup], DefaultPlaceholder] = ...,
        invoke_without_command: Union[bool, DefaultPlaceholder] = ...,
        no_args_is_help: Union[bool, DefaultPlaceholder] = ...,
        subcommand_metavar: Union[str, DefaultPlaceholder] = ...,
        chain: Union[bool, DefaultPlaceholder] = ...,
        result_callback: Union[Callable[..., Any], DefaultPlaceholder] = ...,
        context_settings: Union[Dict[str, Any], DefaultPlaceholder] = ...,
        callback: Union[Callable[..., Any], DefaultPlaceholder] = ...,
        help: Union[str, DefaultPlaceholder] = ...,
        epilog: Union[str, DefaultPlaceholder] = ...,
        short_help: Union[str, DefaultPlaceholder] = ...,
        options_metavar: Union[str, DefaultPlaceholder] = ...,
        add_help_option: Union[bool, DefaultPlaceholder] = ...,
        hidden: Union[bool, DefaultPlaceholder] = ...,
        deprecated: Union[bool, DefaultPlaceholder] = ...,
        rich_help_panel: Union[str, DefaultPlaceholder] = ...,
    ) -> None: ...
    
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

def get_group(typer_instance: Typer) -> TyperGroup: ...
def get_command(typer_instance: Typer) -> Union[TyperGroup, TyperCommand]: ...
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
) -> Tuple[List[click.Parameter], Dict[str, Callable[..., Any]], Optional[str]]: ...

def get_command_from_info(
    command_info: CommandInfo,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: MarkupMode,
) -> TyperCommand: ...

def determine_type_convertor(type_: Type[Any]) -> Optional[Callable[..., Any]]: ...
def param_path_convertor(value: Optional[Any] = None) -> Optional[Path]: ...
def generate_enum_convertor(enum: Type[Enum]) -> Callable[[str], Enum]: ...

def generate_list_convertor(
    convertor: Optional[Callable[..., Any]], default_value: Any
) -> Callable[[List[Any]], Optional[List[Any]]]: ...

def generate_tuple_convertor(
    types: Tuple[Type[Any], ...],
) -> Callable[[Optional[Tuple[Any, ...]]], Optional[Tuple[Any, ...]]]: ...

def get_callback(
    *,
    callback: Optional[Callable[..., Any]] = None,
    params: List[click.Parameter] = [],
    convertors: Optional[Dict[str, Callable[..., Any]]] = None,
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
) -> Tuple[Union[TyperOption, TyperArgument], Optional[Callable[..., Any]]]: ...

def get_param_callback(
    *,
    callback: Optional[Callable[..., Any]] = None,
    convertor: Optional[Callable[..., Any]] = None,
) -> Optional[Callable[..., Any]]: ...

def get_param_completion(
    callback: Optional[Callable[..., Any]] = None,
) -> Optional[Callable[..., Any]]: ...

def run(function: Callable[..., Any]) -> None: ...
def _is_macos() -> bool: ...
def _is_linux_or_bsd() -> bool: ...

def launch(url: str, wait: bool = False, locate: bool = False) -> int: ...