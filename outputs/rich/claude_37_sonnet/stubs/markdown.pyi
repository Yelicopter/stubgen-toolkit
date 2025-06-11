from __future__ import annotations

import sys
from typing import ClassVar, Iterable

from markdown_it import MarkdownIt
from markdown_it.token import Token

if sys.version_info >= (3, 8):
    from typing import get_args
else:
    from typing_extensions import get_args  # pragma: no cover

from rich.table import Table

from . import box
from ._loop import loop_first
from ._stack import Stack
from .console import Console, ConsoleOptions, JustifyMethod, RenderResult
from .containers import Renderables
from .jupyter import JupyterMixin
from .panel import Panel
from .rule import Rule
from .segment import Segment
from .style import Style, StyleStack
from .syntax import Syntax
from .text import Text, TextType

class MarkdownElement:
    new_line: ClassVar[bool]

    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement: ...

    def on_enter(self, context: MarkdownContext) -> None: ...

    def on_text(self, context: MarkdownContext, text: TextType) -> None: ...

    def on_leave(self, context: MarkdownContext) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class UnknownElement(MarkdownElement): ...

class TextElement(MarkdownElement):
    style_name: str
    text: Text

    def on_enter(self, context: MarkdownContext) -> None: ...

    def on_text(self, context: MarkdownContext, text: TextType) -> None: ...

    def on_leave(self, context: MarkdownContext) -> None: ...

class Paragraph(TextElement):
    style_name: str
    justify: JustifyMethod

    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> Paragraph: ...

    def __init__(self, justify: JustifyMethod) -> None: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class Heading(TextElement):
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> Heading: ...

    def on_enter(self, context: MarkdownContext) -> None: ...

    def __init__(self, tag: str) -> None: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class CodeBlock(TextElement):
    style_name: str

    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> CodeBlock: ...

    def __init__(self, lexer_name: str, theme: str) -> None: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class BlockQuote(TextElement):
    style_name: str
    elements: Renderables

    def __init__(self) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class HorizontalRule(MarkdownElement):
    new_line: bool

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class TableElement(MarkdownElement):
    def __init__(self) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class TableHeaderElement(MarkdownElement):
    def __init__(self) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

class TableBodyElement(MarkdownElement):
    def __init__(self) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

class TableRowElement(MarkdownElement):
    def __init__(self) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

class TableDataElement(MarkdownElement):
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement: ...

    def __init__(self, justify: JustifyMethod) -> None: ...

    def on_text(self, context: MarkdownContext, text: TextType) -> None: ...

class ListElement(MarkdownElement):
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> ListElement: ...

    def __init__(self, list_type: str, list_start: int | None) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class ListItem(TextElement):
    style_name: str
    elements: Renderables

    def __init__(self) -> None: ...

    def on_child_close(self, context: MarkdownContext, child: MarkdownElement) -> bool: ...

    def render_bullet(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

    def render_number(
        self, console: Console, options: ConsoleOptions, number: int, last_number: int
    ) -> RenderResult: ...

class Link(TextElement):
    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement: ...

    def __init__(self, text: str, href: str): ...

class ImageItem(TextElement):
    new_line: bool

    @classmethod
    def create(cls, markdown: Markdown, token: Token) -> MarkdownElement: ...

    def __init__(self, destination: str, hyperlinks: bool) -> None: ...

    def on_enter(self, context: MarkdownContext) -> None: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class MarkdownContext:
    def __init__(
        self,
        console: Console,
        options: ConsoleOptions,
        style: Style,
        inline_code_lexer: str | None = None,
        inline_code_theme: str = "monokai",
    ) -> None: ...

    @property
    def current_style(self) -> Style: ...

    def on_text(self, text: str, node_type: str) -> None: ...

    def enter_style(self, style_name: str | Style) -> Style: ...

    def leave_style(self) -> Style: ...

class Markdown(JupyterMixin):
    elements: ClassVar[dict[str, type[MarkdownElement]]]
    inlines: set

    def __init__(
        self,
        markup: str,
        code_theme: str = "monokai",
        justify: JustifyMethod | None = None,
        style: str | Style = "none",
        hyperlinks: bool = True,
        inline_code_lexer: str | None = None,
        inline_code_theme: str | None = None,
    ) -> None: ...

    def _flatten_tokens(self, tokens: Iterable[Token]) -> Iterable[Token]: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...