from typing import TYPE_CHECKING, Any, Dict, Iterable, Optional, Tuple

from .console import Group, RenderableType
from .highlighter import ReprHighlighter
from .jupyter import JupyterMixin
from .panel import Panel
from .pretty import Pretty
from .table import Table
from .text import Text, TextType

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult

def render_scope(
    scope: Dict[str, Any],
    *,
    title: Optional[TextType] = None,
    sort_keys: bool = True,
    indent_guides: bool = False,
    max_length: Optional[int] = None,
    max_string: Optional[int] = None
) -> RenderableType: ...

class Scope(JupyterMixin):
    def __init__(
        self,
        scope: Dict[str, Any],
        *,
        name: Optional[str] = None,
        sort_keys: bool = True,
        indent_guides: bool = False,
        max_length: Optional[int] = None,
        max_string: Optional[int] = None
    ) -> None: ...
    
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...