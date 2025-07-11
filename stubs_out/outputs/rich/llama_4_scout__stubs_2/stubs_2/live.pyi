import abc
from . import get_console as get_console
from .console import Console as Console, ConsoleRenderable as ConsoleRenderable, RenderHook as RenderHook, RenderableType as RenderableType
from .control import Control as Control
from .file_proxy import FileProxy as FileProxy
from .jupyter import JupyterMixin as JupyterMixin
from .live_render import LiveRender as LiveRender, VerticalOverflowMethod as VerticalOverflowMethod
from .screen import Screen as Screen
from .text import Text as Text
from threading import Event as Event, RLock as RLock, Thread as Thread
from types import TracebackType as TracebackType
from typing import Callable, Optional

class Live(JupyterMixin, RenderHook, metaclass=abc.ABCMeta):
    def __init__(self, renderable: RenderableType = ..., *, console: Optional[Console] = ..., screen: bool = ..., auto_refresh: bool = ..., refresh_per_second: float = ..., transient: bool = ..., redirect_stdout: bool = ..., redirect_stderr: bool = ..., vertical_overflow: VerticalOverflowMethod = ..., get_renderable: Optional[Callable[[], RenderableType]] = ...) -> None: ...
