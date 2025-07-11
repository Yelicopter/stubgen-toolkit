from datetime import datetime
from enum import Enum
from pathlib import Path
from types import TracebackType
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)
from uuid import UUID

import click

from .core import MarkupMode, TyperCommand, TyperGroup
from .models import (
    CommandInfo,
    DefaultPlaceholder,
    DeveloperExceptionConfig,
    ParamMeta,
    ParameterInfo,
    TyperInfo,
)

def except_hook(
    exc_type: Type[BaseException], exc_value: BaseException, tb: Optional[TracebackType]
) -> None: ...
def get_install_completion_arguments() -> Tuple[click.Parameter, click.Parameter]: ...

class Typer:
    _add_completion: bool
    rich_markup_mode: MarkupMode
    rich_help_panel: DefaultPlaceholder[Optional[str]]
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
        name: DefaultPlaceholder[Optional[str]] = ...,
        cls: DefaultPlaceholder[Optional[Type[TyperGroup]]] = ...,
        invoke_without_command: DefaultPlaceholder[bool] = ...,
        no_args_is_help: DefaultPlaceholder[bool] = ...,
        subcommand_metavar: DefaultPlaceholder[Optional[str]] = ...,
        chain: DefaultPlaceholder[bool] = ...,
        result_callback: DefaultPlaceholder[Optional[Callable[..., Any]]] = ...,
        context_settings: DefaultPlaceholder[Optional[Dict[str, Any]]] = ...,
        callback: DefaultPlaceholder[Optional[Callable[..., Any]]] = ...,
        help: DefaultPlaceholder[Optional[str]] = ...,
        epilog: DefaultPlaceholder[Optional[str]] = ...,
        short_help: DefaultPlaceholder[Optional[str]] = ...,
        options_metavar: DefaultPlaceholder[str] = ...,
        add_help_option: DefaultPlaceholder[bool] = ...,
        hidden: DefaultPlaceholder[bool] = ...,
        deprecated: DefaultPlaceholder[bool] = ...,
        add_completion: bool = ...,
        rich_markup_mode: DefaultPlaceholder[MarkupMode] = ...,
        rich_help_panel: DefaultPlaceholder[Optional[str]] = ...,
        pretty_exceptions_enable: bool = ...,
        pretty_exceptions_show_locals: bool = ...,
        pretty_exceptions_short: bool = ...,
    ) -> None: ...
    def callback(
        self,
        *,
        cls: DefaultPlaceholder[Optional[Type[TyperGroup]]] = ...,
        invoke_without_command: DefaultPlaceholder[bool] = ...,
        no_args_is_help: DefaultPlaceholder[bool] = ...,
        subcommand_metavar: DefaultPlaceholder[Optional[str]] = ...,
        chain: DefaultPlaceholder[bool] = ...,
        result_callback: DefaultPlaceholder[Optional[Callable[..., Any]]] = ...,
        context_settings: DefaultPlaceholder[Optional[Dict[str, Any]]] = ...,
        help: DefaultPlaceholder[Optional[str]] = ...,
        epilog: DefaultPlaceholder[Optional[str]] = ...,
        short_help: DefaultPlaceholder[Optional[str]] = ...,
        options_metavar: DefaultPlaceholder[str] = ...,
        add_help_option: DefaultPlaceholder[bool] = ...,
        hidden: DefaultPlaceholder[bool] = ...,
        deprecated: DefaultPlaceholder[bool] = ...,
        rich_help_panel: DefaultPlaceholder[Optional[str]] = ...,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def command(
        self,
        name: Optional[str] = ...,
        *,
        cls: Optional[Type[TyperCommand]] = ...,
        context_settings: Optional[Dict[str, Any]] = ...,
        help: Optional[str] = ...,
        epilog: Optional[str] = ...,
        short_help: Optional[str] = ...,
        options_metavar: str = ...,
        add_help_option: bool = ...,
        no_args_is_help: bool = ...,
        hidden: bool = ...,
        deprecated: bool = ...,
        rich_help_panel: DefaultPlaceholder[Optional[str]] = ...,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def add_typer(
        self,
        typer_instance: Typer,
        *,
        name: DefaultPlaceholder[Optional[str]] = ...,
        cls: DefaultPlaceholder[Optional[Type[TyperGroup]]] = ...,
        invoke_without_command: DefaultPlaceholder[bool] = ...,
        no_args_is_help: DefaultPlaceholder[bool] = ...,
        subcommand_metavar: DefaultPlaceholder[Optional[str]] = ...,
        chain: DefaultPlaceholder[bool] = ...,
        result_callback: DefaultPlaceholder[Optional[Callable[..., Any]]] = ...,
        context_settings: DefaultPlaceholder[Optional[Dict[str, Any]]] = ...,
        callback: DefaultPlaceholder[Optional[Callable[..., Any]]] = ...,
        help: DefaultPlaceholder[Optional[str]] = ...,
        epilog: DefaultPlaceholder[Optional[str]] = ...,
        short_help: DefaultPlaceholder[Optional[str]] = ...,
        options_metavar: DefaultPlaceholder[str] = ...,
        add_help_option: DefaultPlaceholder[bool] = ...,
        hidden: DefaultPlaceholder[bool] = ...,
        deprecated: DefaultPlaceholder[bool] = ...,
        rich_help_panel: DefaultPlaceholder[Optional[str]] = ...,
    ) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...

def get_group(typer_instance: Typer) -> TyperGroup: ...
def get_command(typer_instance: Typer) -> click.Command: ...
def solve_typer_info_help(typer_info: TyperInfo) -> Optional[str]: ...
def solve_typer_info_defaults(typer_info: TyperInfo) -> TyperInfo: ...
def get_group_from_info(
    group_info: TyperInfo, *, pretty_exceptions_short: bool, rich_markup_mode: MarkupMode
) -> TyperGroup: ...
def get_command_name(name: str) -> str: ...
def get_params_convertors_ctx_param_name_from_function(
    callback: Optional[Callable[..., Any]]
) -> Tuple[List[click.Parameter], Dict[str, Callable[[Any], Any]], Optional[str]]: ...
def get_command_from_info(
    command_info: CommandInfo,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: MarkupMode,
) -> TyperCommand: ...
def determine_type_convertor(type_: Any) -> Optional[Callable[[Any], Any]]: ...
def param_path_convertor(value: Optional[Any] = ...) -> Optional[Path]: ...
def generate_enum_convertor(enum: Type[Enum]) -> Callable[[Any], Optional[Enum]]: ...
def generate_list_convertor(
    convertor: Optional[Callable[[Any], Any]], default_value: Any
) -> Callable[[List[Any]], Optional[List[Any]]]: ...
def generate_tuple_convertor(
    types: Tuple[Any, ...]
) -> Callable[[Optional[Tuple[Any, ...]]], Optional[Tuple[Any, ...]]]: ...
def get_callback(
    *,
    callback: Optional[Callable[..., Any]] = ...,
    params: List[click.Parameter] = ...,
    convertors: Optional[Dict[str, Callable[[Any], Any]]] = ...,
    context_param_name: Optional[str] = ...,
    pretty_exceptions_short: bool,
) -> Optional[Callable[..., Any]]: ...
def get_click_type(
    *, annotation: Any, parameter_info: ParameterInfo
) -> click.ParamType: ...
def lenient_issubclass(
    cls: Any, class_or_tuple: Union[type, Tuple[type, ...]]
) -> bool: ...
def get_click_param(
    param: ParamMeta,
) -> Tuple[click.Parameter, Optional[Callable[[Any], Any]]]: ...
def get_param_callback(
    *,
    callback: Optional[Callable[..., Any]] = ...,
    convertor: Optional[Callable[[Any], Any]] = ...,
) -> Optional[Callable[[click.Context, click.Parameter, Any], Any]]: ...
def get_param_completion(
    callback: Optional[Callable[..., Any]] = ...,
) -> Optional[
    Callable[[click.Context, List[str], str], List[Union[str, Tuple[str, str]]]]
]: ...
def run(function: Callable[..., Any]) -> None: ...
def launch(url: str, wait: bool = ..., locate: bool = ...) -> int: ...