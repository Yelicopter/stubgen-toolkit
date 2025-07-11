from __future__ import annotations

from typing import Iterable, Sequence, Tuple

from rich.color import ColorTriplet
from rich.console import Console, ConsoleOptions
from rich.segment import Segment
from rich.table import Table

class Palette:
    _colors: Sequence[Tuple[int, int, int]]
    def __init__(self, colors: Sequence[Tuple[int, int, int]]) -> None: ...
    def __getitem__(self, number: int) -> ColorTriplet: ...
    def __rich__(self) -> Table: ...
    def match(self, color: ColorTriplet) -> int: ...

class ColorBox:
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> Iterable[Segment]: ...