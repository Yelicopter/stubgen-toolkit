from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Union

import click
from rich.console import Console

def _get_rich_console(stderr: bool = ...) -> Console: ...
def _make_rich_text(
    *, text: str, style: str = ..., markup_mode: Any
) -> Any: ...
def _get_help_text(
    *,
    obj: Any,
    markup_mode: Any,
) -> Iterable[Any]: ...
def _get_parameter_help(
    *,
    param: Any,
    ctx: Any,
    markup_mode: Any,
) -> Any: ...
def _make_command_help(
    *,
    help_text: str,
    markup_mode: Any,
) -> Any: ...
def _print_options_panel(
    *,
    name: str,
    params: list[Any],
    ctx: Any,
    markup_mode: Any,
    console: Console,
) -> None: ...
def _print_commands_panel(
    *,
    name: str,
    commands: list[Any],
    markup_mode: Any,
    console: Console,
    cmd_len: int,
) -> None: ...
def rich_format_help(
    *,
    obj: Any,
    ctx: Any,
    markup_mode: Any,
) -> None: ...
def rich_format_error(self: Any) -> None: ...
def rich_abort_error() -> None: ...
def rich_to_html(input_text: str) -> str: ...
def rich_render_text(text: str) -> str: ...