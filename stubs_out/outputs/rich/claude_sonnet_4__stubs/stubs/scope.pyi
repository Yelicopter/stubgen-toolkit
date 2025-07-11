from .console import Console as Console, ConsoleOptions as ConsoleOptions, Group as Group, RenderResult as RenderResult, RenderableType as RenderableType
from .highlighter import ReprHighlighter as ReprHighlighter
from .jupyter import JupyterMixin as JupyterMixin
from .panel import Panel as Panel
from .pretty import Pretty as Pretty
from .table import Table as Table
from .text import Text as Text, TextType as TextType
from typing import Any, Dict, Optional

def render_scope(scope: Dict[str, Any], *, title: Optional[TextType] = ..., sort_keys: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ...) -> RenderableType: ...

class Scope(JupyterMixin):
    def __init__(self, scope: Dict[str, Any], *, name: Optional[str] = ..., sort_keys: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
