from math import sqrt
from functools import lru_cache
from typing import Sequence, Tuple, TYPE_CHECKING

from .color_triplet import ColorTriplet

if TYPE_CHECKING:
    from rich.table import Table

class Palette:
    def __init__(self, colors: Sequence[Tuple[int, int, int]]) -> None: ...

    def __getitem__(self, number: int) -> ColorTriplet: ...

    def __rich__(self) -> "Table": ...

    @lru_cache(maxsize=1024)
    def match(self, color: Tuple[int, int, int]) -> int: ...