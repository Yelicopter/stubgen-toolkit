from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Sequence

if TYPE_CHECKING:
    from rich.console import ConsoleRenderable

from . import get_console
from .segment import Segment

if TYPE_CHECKING:
    from rich.console import ConsoleRenderable

JUPYTER_HTML_FORMAT: str

class JupyterRenderable:
    html: str
    text: str

    def __init__(self, html: str, text: str) -> None: ...

    def _repr_mimebundle_(
        self, include: Sequence[str], exclude: Sequence[str], **kwargs: Any
    ) -> Dict[str, str]: ...

class JupyterMixin:
    def _repr_mimebundle_(
        self: "ConsoleRenderable",
        include: Sequence[str],
        exclude: Sequence[str],
        **kwargs: Any,
    ) -> Dict[str, str]: ...

def _render_segments(segments: Iterable[Segment]) -> str: ...

def display(segments: Iterable[Segment], text: str) -> None: ...

def print(*args: Any, **kwargs: Any) -> None: ...