import click
from _typeshed import Incomplete
from rich.columns import Columns as Columns
from rich.console import Console as Console, RenderableType as RenderableType
from rich.highlighter import RegexHighlighter
from rich.text import Text as Text
from typing import List, Union

MarkupMode: Incomplete

class OptionHighlighter(RegexHighlighter):
    highlights: List[str]

class NegativeOptionHighlighter(RegexHighlighter):
    highlights: List[str]

def rich_format_help(*, obj: click.BaseCommand, ctx: click.Context, markup_mode: MarkupMode) -> None: ...
def rich_format_error(self) -> None: ...
def rich_abort_error() -> None: ...
def rich_to_html(input_text: str) -> str: ...
def rich_render_text(text: Union[str, Text]) -> str: ...
