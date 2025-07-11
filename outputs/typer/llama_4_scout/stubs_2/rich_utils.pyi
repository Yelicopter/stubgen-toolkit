from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Union

def _get_rich_console(stderr: bool = False) -> Any:
    ...
def _make_rich_text(
    *,
    text: str,
    style: str = "",
    markup_mode: str,
) -> Any:
    ...
def _get_help_text(
    *,
    obj: Any,
    markup_mode: str,
) -> Any:
    ...
def _get_parameter_help(
    *,
    param: Any,
    ctx: Any,
    markup_mode: str,
) -> Any:
    ...
def _make_command_help(
    *,
    help_text: str,
    markup_mode: str,
) -> Any:
    ...
def _print_options_panel(
    *,
    name: str,
    params: Any,
    ctx: Any,
    markup_mode: str,
    console: Any,
) -> None:
    ...
def _print_commands_panel(
    *,
    name: str,
    commands: Any,
    markup_mode: str,
    console: Any = Any,
) -> None:
    ...