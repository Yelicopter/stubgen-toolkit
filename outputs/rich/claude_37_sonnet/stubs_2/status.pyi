from types import TracebackType
from typing import Optional, Type

from .console import Console, RenderableType
from .jupyter import JupyterMixin
from .live import Live
from .spinner import Spinner
from .style import StyleType

class Status(JupyterMixin):
    def __init__(
        self,
        status: RenderableType,
        *,
        console: Optional[Console] = ...,
        spinner: str = ...,
        spinner_style: StyleType = ...,
        speed: float = ...,
        refresh_per_second: float = ...,
    ) -> None: ...
    status: RenderableType
    spinner_style: StyleType
    speed: float
    _spinner: Spinner
    _live: Live
    @property
    def renderable(self) -> Spinner: ...
    @property
    def console(self) -> Console: ...
    def update(
        self,
        status: Optional[RenderableType] = ...,
        *,
        spinner: Optional[str] = ...,
        spinner_style: Optional[StyleType] = ...,
        speed: Optional[float] = ...,
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def __rich__(self) -> RenderableType: ...
    def __enter__(self) -> "Status": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...