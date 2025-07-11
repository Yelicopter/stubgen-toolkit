import re
from typing import Any, Callable, Dict, Iterable, List, Optional, Union

from ._loop import loop_first
from .console import Console, ConsoleOptions, JustifyMethod, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style, StyleType
from .text import Text

class MarkdownElement:
    def create(self, markdown: "Markdown", node: Any) -> Any: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class UnknownElement(MarkdownElement):
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class TextElement(MarkdownElement):
    style_name: str = "none"
    
    def __init__(self, text: str, style: Optional[StyleType] = None) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class Paragraph(MarkdownElement):
    justify: Optional[JustifyMethod]
    style_name: str = "markdown.paragraph"
    
    def __init__(self, inline: MarkdownElement, justify: Optional[JustifyMethod] = None) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class Heading(MarkdownElement):
    def __init__(self, inline: MarkdownElement, level: int) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class CodeBlock(MarkdownElement):
    style_name: str = "markdown.code_block"
    
    def __init__(self, code: str, lexer_name: str) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class BlockQuote(MarkdownElement):
    style_name: str = "markdown.block_quote"
    
    def __init__(self, quote: MarkdownElement) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class HorizontalRule(MarkdownElement):
    style_name: str = "markdown.hr"
    
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class ListElement(MarkdownElement):
    style_name: str = "markdown.list"

class ListItem(MarkdownElement):
    style_name: str = "markdown.item"
    
    def __init__(self, element: MarkdownElement) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

class Markdown(JupyterMixin):
    elements: Dict[str, Callable[[Any], MarkdownElement]] = ...
    inlines: Dict[str, Callable[[Any], MarkdownElement]] = ...
    
    def __init__(
        self,
        markup: str,
        code_theme: str = "monokai",
        justify: Optional[JustifyMethod] = None,
        style: StyleType = "none",
        hyperlinks: bool = True,
        inline_code_lexer: Optional[str] = None,
        inline_code_theme: Optional[str] = None
    ) -> None: ...
    
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...