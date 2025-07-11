from .console import ConsoleRenderable as ConsoleRenderable
from .highlighter import ReprHighlighter as ReprHighlighter
from .panel import Panel as Panel
from .pretty import Pretty as Pretty
from .table import Table as Table
from .text import Text as Text, TextType as TextType
from collections.abc import Mapping
from typing import Optional

def render_scope(scope: Mapping, *, title: Optional[str] = ..., sort_keys: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ...) -> ConsoleRenderable: ...
