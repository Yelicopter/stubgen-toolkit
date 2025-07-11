from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Optional, Tuple

from .highlighter import ReprHighlighter
from .panel import Panel
from .pretty import Pretty
from .table import Table
from .text import Text, TextType

if TYPE_CHECKING:
    from .console import ConsoleRenderable


def render_scope(
    scope: Mapping,
    *,
    title: Optional[str] = None,
    sort_keys: bool = True,
    indent_guides: bool = False,
    max_length: Optional[int] = None,
    max_string: Optional[int] = None,
) -> "ConsoleRenderable":
    ...