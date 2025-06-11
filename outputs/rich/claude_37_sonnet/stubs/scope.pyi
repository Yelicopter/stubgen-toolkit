from collections.abc import Mapping
from typing import Any, Optional, Tuple

from .highlighter import ReprHighlighter
from .panel import Panel
from .pretty import Pretty
from .table import Table
from .text import Text, TextType
from .console import ConsoleRenderable

def render_scope(
    scope: Mapping[str, Any],
    *,
    title: Optional[TextType] = ...,
    sort_keys: bool = ...,
    indent_guides: bool = ...,
    max_length: Optional[int] = ...,
    max_string: Optional[int] = ...,
) -> ConsoleRenderable: ...