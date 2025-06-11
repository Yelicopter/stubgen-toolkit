from typing import TYPE_CHECKING, List, Optional, Tuple, Union

if TYPE_CHECKING:
    from .console import (
        Console,
        ConsoleOptions,
        RenderableType,
        RenderResult,
    )

from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style

PaddingDimensions = Union[int, Tuple[int], Tuple[int, int], Tuple[int, int, int, int]]

class Padding(JupyterMixin):
    def __init__(
        self,
        renderable: "RenderableType",
        pad: "PaddingDimensions" = (0, 0, 0, 0),
        *,
        style: Union[str, Style] = "none",
        expand: bool = True,
    ) -> None: ...

    @classmethod
    def indent(cls, renderable: "RenderableType", level: int) -> "Padding": ...

    @staticmethod
    def unpack(pad: "PaddingDimensions") -> Tuple[int, int, int, int]: ...

    def __repr__(self) -> str: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "Measurement": ...