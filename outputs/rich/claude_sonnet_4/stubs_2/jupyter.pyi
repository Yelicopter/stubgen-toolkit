from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Sequence

if TYPE_CHECKING:
    from rich.console import ConsoleRenderable

from . import get_console
from .segment import Segment
from .terminal_theme import DEFAULT_TERMINAL_THEME

class JupyterRenderable:
    def __init__(self, html: str, text: str) -> None: ...
    def _repr_mimebundle_(self, include: Any, exclude: Any, **kwargs: Any) -> Dict[str, str]: ...

class JupyterMixin:
    __slots__ = ()
    
    def _repr_mimebundle_(self, include: Any, exclude: Any, **kwargs: Any) -> Dict[str, str]: ...

def display(segments: Iterable[Segment], text: str) -> None: ...
def print(*args: Any, **kwargs: Any) -> None: ...