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
    """A thread that calls refresh() at regular intervals."""

    def __init__(self, live: "Live", refresh_per_second: float):
        ...

    def stop(self) -> None:
        ...

    def run(self) -> None:
        ...


class Live(JupyterMixin, RenderHook):
    """Renders an auto-updating live display of any given renderable.

    Args:
        renderable (RenderableType, optional): The renderable to live display. Defaults to displaying nothing.
        console (Console, optional): Optional Console instance. Defaults to an internal Console instance writing to stdout.
        screen (bool, optional): Enable alternate screen mode. Defaults to False.
        auto_refresh (bool, optional): Enable auto refresh. If disabled, you will need to call `refresh()` or `update()` with refresh flag. Defaults to True
        refresh_per_second (float, optional): Number of times per second to refresh the live display. Defaults to 4.
        transient (bool, optional): Clear the renderable on exit (has no effect when screen=True). Defaults to False.
        redirect_stdout (bool, optional): Enable redirection of stdout, so ``print`` may be used. Defaults to True.
        redirect_stderr (bool, optional): Enable redirection of stderr. Defaults to True.
        vertical_overflow (VerticalOverflowMethod, optional): How to handle renderable when it is too tall for the console. Defaults to "ellipsis".
        get_renderable (Callable[[], RenderableType], optional): Optional callable to get renderable. Defaults to None.
    """

    def __init__(
        self,
        renderable: RenderableType = None,
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
    ):
        ...

    @property
    def is_started(self) -> bool:
        """Check if live display has been started."""
        ...

    def get_renderable(self) -> RenderableType:
        ...

    def start(self, refresh: bool = False) -> None:
        """Start live rendering display.

        Args:
            refresh (bool, optional): Also refresh. Defaults to False.
        """
        ...

    def stop(self) -> None:
        """Stop live rendering display."""
        ...

    def __enter__(self) -> "Live":
        ...

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        ...

    def _enable_redirect_io(self) -> None:
        """Enable redirecting of stdout / stderr."""
        ...

    def _disable_redirect_io(self) -> None:
        """Disable redirecting of stdout / stderr."""
        ...

    @property
    def renderable(self) -> RenderableType:
        """Get the renderable that is being displayed

        Returns:
            RenderableType: Displayed renderable.
        """
        ...

    def update(self, renderable: RenderableType, *, refresh: bool = False) -> None:
        """Update the renderable that is being displayed

        Args:
            renderable (RenderableType): New renderable to use.
            refresh (bool, optional): Refresh the display. Defaults to False.
        """
        ...

    def refresh(self) -> None:
        """Update the display of the Live Render."""
        ...

    def process_renderables(
        self, renderables: Iterable[RenderableType]
    ) -> Iterable[RenderableType]:
        """Process renderables to restore cursor and display progress."""
        ...
