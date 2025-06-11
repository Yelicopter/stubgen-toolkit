from operator import itemgetter
from typing import TYPE_CHECKING, Callable, NamedTuple, Optional, Sequence

from . import errors
from .protocol import is_renderable, rich_cast

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType

class Measurement(NamedTuple):
    minimum: int
    maximum: int

    @property
    def span(self) -> int: ...

    def normalize(self) -> "Measurement": ...

    def with_maximum(self, width: int) -> "Measurement": ...

    def with_minimum(self, width: int) -> "Measurement": ...

    def clamp(
        self, min_width: Optional[int] = None, max_width: Optional[int] = None
    ) -> "Measurement": ...

    @classmethod
    def get(
        cls, console: "Console", options: "ConsoleOptions", renderable: "RenderableType"
    ) -> "Measurement": ...

def measure_renderables(
    console: "Console",
    options: "ConsoleOptions",
    renderables: Sequence["RenderableType"],
) -> "Measurement": ...