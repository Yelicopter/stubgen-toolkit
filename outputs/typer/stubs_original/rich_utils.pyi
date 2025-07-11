import click
from _typeshed import Incomplete
from rich.console import RenderableType as RenderableType
from rich.highlighter import RegexHighlighter
from typing import Literal, Optional, Union

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
ALIGN_OPTIONS_PANEL: Literal['left', 'center', 'right']
STYLE_OPTIONS_TABLE_SHOW_LINES: bool
STYLE_OPTIONS_TABLE_LEADING: int
STYLE_OPTIONS_TABLE_PAD_EDGE: bool
STYLE_OPTIONS_TABLE_PADDING: Incomplete
STYLE_OPTIONS_TABLE_BOX: str
STYLE_OPTIONS_TABLE_ROW_STYLES: Incomplete
STYLE_OPTIONS_TABLE_BORDER_STYLE: Incomplete
STYLE_COMMANDS_PANEL_BORDER: str
ALIGN_COMMANDS_PANEL: Literal['left', 'center', 'right']
STYLE_COMMANDS_TABLE_SHOW_LINES: bool
STYLE_COMMANDS_TABLE_LEADING: int
STYLE_COMMANDS_TABLE_PAD_EDGE: bool
STYLE_COMMANDS_TABLE_PADDING: Incomplete
STYLE_COMMANDS_TABLE_BOX: str
STYLE_COMMANDS_TABLE_ROW_STYLES: Incomplete
STYLE_COMMANDS_TABLE_BORDER_STYLE: Incomplete
STYLE_COMMANDS_TABLE_FIRST_COLUMN: str
STYLE_ERRORS_PANEL_BORDER: str
ALIGN_ERRORS_PANEL: Literal['left', 'center', 'right']
STYLE_ERRORS_SUGGESTION: str
STYLE_ABORTED: str
MAX_WIDTH: Incomplete
COLOR_SYSTEM: Optional[Literal['auto', 'standard', '256', 'truecolor', 'windows']]
FORCE_TERMINAL: Incomplete
DEPRECATED_STRING: Incomplete
DEFAULT_STRING: Incomplete
ENVVAR_STRING: Incomplete
REQUIRED_SHORT_STRING: str
REQUIRED_LONG_STRING: Incomplete
RANGE_STRING: str
ARGUMENTS_PANEL_TITLE: Incomplete
OPTIONS_PANEL_TITLE: Incomplete
COMMANDS_PANEL_TITLE: Incomplete
ERRORS_PANEL_TITLE: Incomplete
ABORTED_TEXT: Incomplete
RICH_HELP: Incomplete
MARKUP_MODE_MARKDOWN: str
MARKUP_MODE_RICH: str
MarkupMode: Incomplete

class OptionHighlighter(RegexHighlighter):
    highlights: Incomplete

class NegativeOptionHighlighter(RegexHighlighter):
    highlights: Incomplete

highlighter: Incomplete
negative_highlighter: Incomplete

def rich_format_help(*, obj: Union[click.Command, click.Group], ctx: click.Context, markup_mode: MarkupMode) -> None: ...
def rich_format_error(self) -> None: ...
def rich_abort_error() -> None: ...
def rich_to_html(input_text: str) -> str: ...
def rich_render_text(text: str) -> str: ...
