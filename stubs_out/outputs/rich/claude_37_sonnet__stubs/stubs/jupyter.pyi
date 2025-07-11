from . import get_console as get_console
from .segment import Segment as Segment
from rich.console import ConsoleRenderable as ConsoleRenderable
from typing import Any, Iterable

JUPYTER_HTML_FORMAT: str

class JupyterRenderable:
    html: str
    text: str
    def __init__(self, html: str, text: str) -> None: ...

class JupyterMixin: ...

def display(segments: Iterable[Segment], text: str) -> None: ...
def print(*args: Any, **kwargs: Any) -> None: ...
