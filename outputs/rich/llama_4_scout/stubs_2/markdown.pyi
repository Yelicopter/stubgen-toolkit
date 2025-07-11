from __future__ import annotations
import sys
from typing import ClassVar, Iterable
from markdown_it import MarkdownIt
from markdown_it.token import Token

if sys.version_info >= (3, 8):
    from typing import get_args
else:
    from typing_extensions import get_args  # pragma: no cover

class JupyterMixin:
    ...

class MarkdownElement:
    ...

class UnknownElement(MarkdownElement):
    ...

class TextElement(MarkdownElement):
    ...

class Paragraph(TextElement):
    ...

class Heading(TextElement):
    ...

class CodeBlock(TextElement):
    ...

class BlockQuote(TextElement):
    ...

class HorizontalRule(MarkdownElement):
    ...

class TableElement(MarkdownElement):
    ...

class TableHeaderElement(MarkdownElement):
    ...

class TableBodyElement(MarkdownElement):
    ...

class TableRowElement(MarkdownElement):
    ...

class TableDataElement(MarkdownElement):
    ...

class ListElement(MarkdownElement):
    ...

class ListItem(TextElement):
    ...

class Link(TextElement):
    ...

class ImageItem(TextElement):
    ...

class MarkdownContext:
    ...

class Markdown(JupyterMixin):
    ...