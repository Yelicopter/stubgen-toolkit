from types import TracebackType
from typing import Optional, Type

from .console import Console, RenderableType
from .jupyter import JupyterMixin
from .live import Live
from .spinner import Spinner
from .style import StyleType

class Status(JupyterMixin):
    """Displays a status indicator with a 'spinner' animation.

    Args:
        status (RenderableType): A status renderable (str or Text typically).
        console (Console, optional): Console instance to use, or None for global console. Defaults to None.
        spinner (str, optional): Name of spinner animation (see python -m rich.spinner). Defaults to "dots".
        spinner_style (StyleType, optional): Style of spinner. Defaults to "status.spinner".
        speed (float, optional): Speed factor for spinner animation. Defaults to 1.0.
        refresh_per_second (float, optional): Number of refreshes per second. Defaults to 12.5.
    """

    def __init__(
        self,
        status: RenderableType,
        *,
        console: Optional[Console] = None,
        spinner: str = "dots",
        spinner_style: StyleType = "status.spinner",
        speed: float = 1.0,
        refresh_per_second: float = 12.5,
    ) -> None:
        ...

    @property
    def renderable(self) -> "Spinner":
        ...

    @property
    def console(self) -> Console:
        ...

    def update(
        self,
        status: Optional[RenderableType] = None,
        *,
        spinner: Optional[str] = None,
        spinner_style: Optional[StyleType] = None,
        speed: Optional[float] = None,
    ) -> None:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

    def __rich__(self) -> "Spinner":
        ...

    def __enter__(self) -> "Status":
        ...

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None:
        ...