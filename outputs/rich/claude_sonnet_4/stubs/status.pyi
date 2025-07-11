from types import TracebackType
from typing import Optional, Type, Union

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
        console: Optional[Console] = None,
        spinner: str = "dots",
        spinner_style: StyleType = "status.spinner",
        speed: float = 1.0,
        refresh_per_second: float = 12.5
    ) -> None: ...
    
    @property
    def renderable(self) -> RenderableType: ...
    
    def update(
        self,
        status: Optional[RenderableType] = None,
        *,
        spinner: Optional[str] = None,
        spinner_style: Optional[StyleType] = None,
        speed: Optional[float] = None
    ) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def __enter__(self) -> "Status": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...