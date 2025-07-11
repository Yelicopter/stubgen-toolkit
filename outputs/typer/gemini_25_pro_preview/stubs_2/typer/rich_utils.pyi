from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Union

import click
import click.core
from rich.columns import Columns
from rich.console import Console, RenderableType
from rich.highlighter import RegexHighlighter
from rich.text import Text
from typing_extensions import Literal

MarkupMode = Literal["markdown", "rich", None]

class OptionHighlighter(RegexHighlighter):
    highlights: List[str]

class NegativeOptionHighlighter(RegexHighlighter):
    highlights: List[str]

def _get_rich_console(stderr: bool = ...) -> Console: ...
def _make_rich_text(
    *, text: str, style: str = ..., markup_mode: MarkupMode
) -> RenderableType: ...
def _get_help_text(
    *, obj: click.core.BaseCommand, markup_mode: MarkupMode
) -> RenderableType: ...
def _get_parameter_help(
    *,
    param: Union[click.Option, click.Argument],
    ctx: click.Context,
    markup_mode: MarkupMode,
) -> Columns: ...
def _make_command_help(
    *, help_text: str, markup_mode: MarkupMode
) -> RenderableType: ...
def _print_options_panel(
    *,
    name: str,
    params: List[Union[click.Option, click.Argument]],
    ctx: click.Context,
    markup_mode: MarkupMode,
    console: Console,
) -> None: ...
def _print_commands_panel(
    *,
    name: str,
    commands: List[click.Command],
    markup_mode: MarkupMode,
    console: Console,
    cmd_len: int,
) -> None: ...
def rich_format_help(
    *, obj: click.core.BaseCommand, ctx: click.Context, markup_mode: MarkupMode
) -> None: ...
def rich_format_error(self: click.ClickException) -> None: ...
def rich_abort_error() -> None: ...
def rich_to_html(input_text: str) -> str: ...
def rich_render_text(text: Union[str, Text]) -> str: ...