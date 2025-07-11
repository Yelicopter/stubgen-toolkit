from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Type, Union
from uuid import UUID
import click
from typer._types import TyperChoice

def get_group(
    typer_instance: Any,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: str,
) -> Any:
    ...
def get_command(
    typer_instance: Any,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: str,
) -> Any:
    ...
def solve_typer_info_help(typer_info: Any) -> str:
    ...
def solve_typer_info_defaults(typer_info: Any) -> Any:
    ...
def get_group_from_info(
    group_info: Any,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: str,
) -> Any:
    ...
def get_command_from_info(
    command_info: Any,
    *,
    pretty_exceptions_short: bool,
    rich_markup_mode: str,
) -> Any:
    ...
def determine_type_convertor(type_: Type) -> Any:
    ...
def param_path_convertor(value: Any = None) -> Any:
    ...
def generate_enum_convertor(enum: Any) -> Any:
    ...
def generate_list_convertor(
    convertor: Any,
    default_value: Any,
) -> Any:
    ...
def generate_tuple_convertor(types: Any) -> Any:
    ...
def get_click_type(
    *,
    annotation: Any,
    parameter_info: Any,
) -> Any:
    ...
def lenient_issubclass(cls: Any, class_or_tuple: Any) -> bool:
    ...
def get_click_param(
    param: Any,
) -> Tuple[Any, Any]:
    ...
def get_param_callback(
    *,
    callback: Callable = None,
    convertor: Any = None,
) -> Callable:
    ...
def get_param_completion(
    callback: Callable = None,
) -> Callable:
    ...
def run(function: Callable) -> None:
    ...