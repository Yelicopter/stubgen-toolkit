from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Type, Union
from uuid import UUID
from datetime import datetime
from pathlib import Path
from enum import Enum

from .models import (
    TyperInfo,
    CommandInfo,
    ParameterInfo,
    OptionInfo,
    ArgumentInfo,
    FileText,
    FileTextWrite,
    FileBinaryRead,
    FileBinaryWrite,
    NoneType,
    Default,
    DefaultPlaceholder,
    DeveloperExceptionConfig,
    TyperPath,
    ParamMeta,
    CommandFunctionType,
    AnyType,
    Required,
)
from .core import MarkupMode

def except_hook(
    exc_type: type[BaseException], exc_value: BaseException, tb: Any
) -> None: ...
def get_install_completion_arguments() -> tuple[Any, Any]: ...

class Typer:
    _add_completion: bool
    rich_markup_mode: Any
    rich_help_panel: Any
    pretty_exceptions_enable: bool
    pretty_exceptions_show_locals: bool
    pretty_exceptions_short: bool
    info: TyperInfo
    registered_groups: list[Any]
    registered_commands: list[Any]
    registered_callback: Any
    def __init__(
        self,
        *,
        name: Any = ...,
        cls: Any = ...,
        invoke_without_command: Any = ...,
        no_args_is_help: Any = ...,
        subcommand_metavar: Any = ...,
        chain: Any = ...,
        result_callback: Any = ...,
        context_settings: Any = ...,
        callback: Any = ...,
        help: Any = ...,
        epilog: Any = ...,
        short_help: Any = ...,
        options_metavar: Any = ...,
        add_help_option: Any = ...,
        hidden: Any = ...,
        deprecated: Any = ...,
        add_completion: bool = ...,
        rich_markup_mode: Any = ...,
        rich_help_panel: Any = ...,
        pretty_exceptions_enable: bool = ...,
        pretty_exceptions_show_locals: bool = ...,
        pretty_exceptions_short: bool = ...,
    ) -> None: ...
    def callback(
        self,
        *,
        cls: Any = ...,
        invoke_without_command: Any = ...,
        no_args_is_help: Any = ...,
        subcommand_metavar: Any = ...,
        chain: Any = ...,
        result_callback: Any = ...,
        context_settings: Any = ...,
        help: Any = ...,
        epilog: Any = ...,
        short_help: Any = ...,
        options_metavar: Any = ...,
        add_help_option: Any = ...,
        hidden: Any = ...,
        deprecated: Any = ...,
        rich_help_panel: Any = ...,
    ) -> Callable[[Any], Any]: ...
    def command(
        self,
        name: Any = ...,
        *,
        cls: Any = ...,
        context_settings: Any = ...,
        help: Any = ...,
        epilog: Any = ...,
        short_help: Any = ...,
        options_metavar: Any = ...,
        add_help_option: Any = ...,
        no_args_is_help: Any = ...,
        hidden: Any = ...,
        deprecated: Any = ...,
        rich_help_panel: Any = ...,
    ) -> Callable[[Any], Any]: ...
    def add_typer(
        self,
        typer_instance: "Typer",
        *,
        name: Any = ...,
        cls: Any = ...,
        invoke_without_command: Any = ...,
        no_args_is_help: Any = ...,
        subcommand_metavar: Any = ...,
        chain: Any = ...,
        result_callback: Any = ...,
        context_settings: Any = ...,
        callback: Any = ...,
        help: Any = ...,
        epilog: Any = ...,
        short_help: Any = ...,
        options_metavar: Any = ...,
        add_help_option: Any = ...,
        hidden: Any = ...,
        deprecated: Any = ...,
        rich_help_panel: Any = ...,
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

def get_group(typer_instance: Typer) -> Any: ...
def get_command(typer_instance: Typer) -> Any: ...
def solve_typer_info_help(typer_info: TyperInfo) -> str: ...
def solve_typer_info_defaults(typer_info: TyperInfo) -> TyperInfo: ...
def get_group_from_info(
    group_info: TyperInfo,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: Any,
) -> Any: ...
def get_command_name(name: str) -> str: ...
def get_params_convertors_ctx_param_name_from_function(
    callback: Any,
) -> tuple[list[Any], dict[str, Any], Optional[str]]: ...
def get_command_from_info(
    command_info: CommandInfo,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: Any,
) -> Any: ...
def determine_type_convertor(type_: Any) -> Any: ...
def param_path_convertor(value: Any = ...) -> Optional[Path]: ...
def generate_enum_convertor(enum: type[Enum]) -> Callable[[Any], Any]: ...
def generate_list_convertor(
    convertor: Any, default_value: Any
) -> Callable[[Any], Any]: ...
def generate_tuple_convertor(
    types: Any,
) -> Callable[[Any], Any]: ...
def get_callback(
    *,
    callback: Any = ...,
    params: list[Any] = ...,
    convertors: dict[str, Any] = ...,
    context_param_name: Optional[str] = ...,
    pretty_exceptions_short: bool,
) -> Any: ...
def get_click_type(
    *, annotation: Any, parameter_info: ParameterInfo
) -> Any: ...
def lenient_issubclass(
    cls: Any, class_or_tuple: Any
) -> bool: ...
def get_click_param(
    param: Any,
) -> tuple[Any, Any]: ...
def get_param_callback(
    *,
    callback: Any = ...,
    convertor: Any = ...,
) -> Any: ...
def get_param_completion(
    callback: Any = ...,
) -> Any: ...
def run(function: Callable[..., Any]) -> None: ...
def _is_macos() -> bool: ...
def _is_linux_or_bsd() -> bool: ...
def launch(url: str, wait: bool = ..., locate: bool = ...) -> int: ...