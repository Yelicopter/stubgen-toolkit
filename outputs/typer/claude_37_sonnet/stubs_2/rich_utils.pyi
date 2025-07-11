import inspect
import io
import sys
from collections import defaultdict
from gettext import gettext as _
from os import getenv
from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Union, Tuple, Literal

import click
from rich import box
from rich.align import Align
from rich.columns import Columns
from rich.console import Console, RenderableType, group
from rich.emoji import Emoji
from rich.highlighter import RegexHighlighter
from rich.markdown import Markdown
from rich.padding import Padding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal

MarkupMode = Optional[Literal["markdown", "rich"]]

STYLE_OPTION: str
STYLE_SWITCH: str
STYLE_NEGATIVE_OPTION: str
STYLE_NEGATIVE_SWITCH: str
STYLE_METAVAR: str
STYLE_METAVAR_SEPARATOR: str
STYLE_USAGE: str
STYLE_USAGE_COMMAND: str
STYLE_DEPRECATED: str
STYLE_DEPRECATED_COMMAND: str
STYLE_HELPTEXT_FIRST_LINE: str
STYLE_HELPTEXT: str
STYLE_OPTION_HELP: str
STYLE_OPTION_DEFAULT: str
STYLE_OPTION_ENVVAR: str
STYLE_REQUIRED_SHORT: str
STYLE_REQUIRED_LONG: str
STYLE_OPTIONS_PANEL_BORDER: str
ALIGN_OPTIONS_PANEL: Literal["left", "center", "right"]
STYLE_OPTIONS_TABLE_SHOW_LINES: bool
STYLE_OPTIONS_TABLE_LEADING: int
STYLE_OPTIONS_TABLE_PAD_EDGE: bool
STYLE_OPTIONS_TABLE_PADDING: Tuple[int, int]
STYLE_OPTIONS_TABLE_BOX: str
STYLE_OPTIONS_TABLE_ROW_STYLES: Optional[List[str]]
STYLE_OPTIONS_TABLE_BORDER_STYLE: Optional[str]
STYLE_COMMANDS_PANEL_BORDER: str
ALIGN_COMMANDS_PANEL: Literal["left", "center", "right"]
STYLE_COMMANDS_TABLE_SHOW_LINES: bool
STYLE_COMMANDS_TABLE_LEADING: int
STYLE_COMMANDS_TABLE_PAD_EDGE: bool
STYLE_COMMANDS_TABLE_PADDING: Tuple[int, int]
STYLE_COMMANDS_TABLE_BOX: str
STYLE_COMMANDS_TABLE_ROW_STYLES: Optional[List[str]]
STYLE_COMMANDS_TABLE_BORDER_STYLE: Optional[str]
STYLE_COMMANDS_TABLE_FIRST_COLUMN: str
STYLE_ERRORS_PANEL_BORDER: str
ALIGN_ERRORS_PANEL: Literal["left", "center", "right"]
STYLE_ERRORS_SUGGESTION: str
STYLE_ABORTED: str
MAX_WIDTH: Optional[int]
COLOR_SYSTEM: Optional[Literal["auto", "standard", "256", "truecolor", "windows"]]
FORCE_TERMINAL: Optional[bool]

DEPRECATED_STRING: str
DEFAULT_STRING: str
ENVVAR_STRING: str
REQUIRED_SHORT_STRING: str
REQUIRED_LONG_STRING: str
RANGE_STRING: str
ARGUMENTS_PANEL_TITLE: str
OPTIONS_PANEL_TITLE: str
COMMANDS_PANEL_TITLE: str
ERRORS_PANEL_TITLE: str
ABORTED_TEXT: str
RICH_HELP: str

MARKUP_MODE_MARKDOWN: str
MARKUP_MODE_RICH: str
_RICH_HELP_PANEL_NAME: str

class OptionHighlighter(RegexHighlighter):
    highlights: List[str]

class NegativeOptionHighlighter(RegexHighlighter):
    highlights: List[str]

highlighter: OptionHighlighter
negative_highlighter: NegativeOptionHighlighter

def _get_rich_console(stderr: bool = False) -> Console: ...
def _make_rich_text(
    *, text: str, style: str = "", markup_mode: MarkupMode
) -> Union[Text, Markdown]: ...

@group()
def _get_help_text(
    *,
    obj: Union[click.Command, click.Group],
    markup_mode: MarkupMode,
) -> Iterable[Union[Text, Markdown]]: ...
def _get_parameter_help(
    *,
    param: Union[click.Option, click.Argument],
    ctx: click.Context,
    markup_mode: MarkupMode,
) -> Columns: ...
def _make_command_help(
    *,
    help_text: str,
    markup_mode: MarkupMode,
) -> Union[Text, Markdown]: ...
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
    *,
    obj: Union[click.Command, click.Group],
    ctx: click.Context,
    markup_mode: MarkupMode,
) -> None: ...
def rich_format_error(self: click.ClickException) -> None: ...
def rich_abort_error() -> None: ...
def rich_to_html(input_text: str) -> str: ...
def rich_render_text(text: str) -> str: ...