from typing import cast, List, Optional, TYPE_CHECKING, Union

from ._spinners import SPINNERS
from .measure import Measurement
from .table import Table
from .text import Text

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult, RenderableType
    from .style import StyleType


class Spinner:
    """A spinner animation.

    Args:
        name (str): Name of spinner (run python -m rich.spinner).
        text (RenderableType, optional): A renderable to display at the right of the spinner (str or Text typically). Defaults to "".
        style (StyleType, optional): Style for spinner animation. Defaults to None.
        speed (float, optional): Speed factor for animation. Defaults to 1.0.

    Raises:
        KeyError: If name isn't one of the supported spinner animations.
    """

    def __init__(
        self,
        name: str,
        text: "RenderableType" = "",
        *,
        style: Optional[StyleType] = None,
        speed: float = 1.0,
    ) -> None:
        ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult":
        ...

    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> Measurement:
        ...

    def render(self, time: float) -> "RenderableType":
        ...

    def update(
        self,
        *,
        text: "RenderableType" = "",
        style: Optional[StyleType] = None,
        speed: Optional[float] = None,
    ) -> None:
        ...