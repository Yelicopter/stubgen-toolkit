from __future__ import annotations

from typing import Iterable, Iterator, Tuple

from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.measure import Measurement
from rich.segment import Segment
from rich.table import Table

class ColorBox:
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> Iterator[Segment]: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

def make_test_card() -> Table: ...
def comparison(renderable1: RenderableType, renderable2: RenderableType) -> Table: ...
