from typing import TYPE_CHECKING, Any, Dict, Iterable, List, Sequence

if TYPE_CHECKING:
    from rich.console import ConsoleRenderable

from jupyter import JupyterMixin
from .live_render import LiveRender, VerticalOverflowMethod
from .screen import Screen
from .text import Text


class _RefreshThread(Thread):
    ...

class Live(JupyterMixin, RenderHook):
    ...