import sys
from threading import Event, RLock, Thread
from types import TracebackType
from typing import IO, Any, Callable, List, Optional, TextIO, Type, cast

from . import get_console
from .console import Console, ConsoleRenderable, RenderableType, RenderHook
from .control import Control
from .file_proxy import FileProxy
from .jupyter import JupyterMixin
from .live_render import LiveRender, VerticalOverflowMethod
from .screen import Screen
from .text import Text

class _RefreshThread(Thread):
    def __init__(self, live: "Live", refresh_per_second: float) -> None: ...

    def stop(self) -> None: ...

    def run(self) -> None: ...

class Live(JupyterMixin, RenderHook):
    def __init__(
        self,
        renderable: Optional[RenderableType] = None,
        *,
        console: Optional[Console] = None,
        screen: bool = False,
        auto_refresh: bool = True,
        refresh_per_second: float = 4,
        transient: bool = False,
        redirect_stdout: bool = True,
        redirect_stderr: bool = True,
        vertical_overflow: VerticalOverflowMethod = "ellipsis",
        get_renderable: Optional[Callable[[], RenderableType]] = None,
    ) -> None: ...

    @property
    def is_started(self) -> bool: ...

    def get_renderable(self) -> RenderableType: ...

    def start(self, refresh: bool = False) -> None: ...

    def stop(self) -> None: ...

    def __enter__(self) -> "Live": ...

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

    def _enable_redirect_io(self) -> None: ...

    def _disable_redirect_io(self) -> None: ...

    @property
    def renderable(self) -> RenderableType: ...

    def update(self, renderable: RenderableType, *, refresh: bool = False) -> None: ...

    def refresh(self) -> None: ...

    def process_renderables(
        self, renderables: List[ConsoleRenderable]
    ) -> List[ConsoleRenderable]: ...