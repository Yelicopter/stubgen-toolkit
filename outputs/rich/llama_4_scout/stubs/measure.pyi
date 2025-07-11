from operator import itemgetter
from typing import TYPE_CHECKING, Callable, NamedTuple, Optional, Sequence

from . import errors
from .protocol import is_renderable, rich_cast

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType


class Measurement(NamedTuple):
    ...

def measure_renderables(
    console: 'Console',
    options: 'ConsoleOptions',
    renderables: Sequence['RenderableType'],
) -> 'Measurement':
    ...