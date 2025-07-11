from __future__ import annotations

from typing import Any, Dict, Iterable, Optional

from rich.console import ConsoleRenderable
from rich.segment import Segment

JUPYTER_HTML_FORMAT: str

class JupyterRenderable:
    html: str
    text: str
    def __init__(self, html: str, text: str) -> None: ...
    def _repr_mimebundle_(self, include: Optional[Iterable[str]], exclude: Optional[Iterable[str]], **kwargs: Any) -> Dict[str, str]: ...

class JupyterMixin:
    def _repr_mimebundle_(self, include: Optional[Iterable[str]], exclude: Optional[Iterable[str]], **kwargs: Any) -> Dict[str, str]: ...

def _render_segments(segments: Iterable[Segment]) -> str: ...
def display(segments: Iterable[Segment], text: str) -> None: ...
def print(*args: Any, **kwargs: Any) -> None: ...