from __future__ import annotations

from functools import lru_cache
from typing import Callable

from ._cell_widths import CELL_WIDTHS


# Ranges of unicode ordinals that produce a1-cell wide character
# This is non-exhaustive, but covers most common Western characters
_SINGLE_CELL_UNICODE_RANGES = [
 (0x20,0x7E), # Latin (excluding non-printable)
 (0xA0,0xAC),
 (0xAE,0x002FF),
 (0x00370,0x00482), # Greek / Cyrillic
 (0x02500,0x025FC), # Box drawing, box elements, geometric shapes
 (0x02800,0x028FF), # Braille
]

# A set of characters that are a single cell wide
_SINGLE_CELLS = frozenset(
 [
 character
 for _start, _end in _SINGLE_CELL_UNICODE_RANGES
 for character in map(chr, range(_start, _end +1))
 ]
)

# When called with a string this will return True if all
# characters are single-cell, otherwise False
_is_single_cell_widths = _SINGLE_CELLS.issuperset


@lru_cache(maxsize=4096)
def cached_cell_len(text: str) -> int:
 """Get the number of cells required to display text.

 This method always caches, which may use up a lot of memory. It is recommended to use
 `cell_len` over this method.

 Args:
 text (str): Text to display.

 Returns:
 int: Get the number of cells required to display text.
 """
 ... 


def cell_len(text: str, _cell_len: Callable[[str], int] = cached_cell_len) -> int:
 """Get the number of cells required to display text.

 Args:
 text (str): Text to display.

 Returns:
 int: Get the number of cells required to display text.
 """
 ... 


@lru_cache(maxsize=4096)
def get_character_cell_size(character: str) -> int:
 """Get the cell size of a character.

 Args:
 character (str): A single character.

 Returns:
 int: Number of cells (0,1 or2) occupied by that character.
 """
 ... 


def set_cell_size(text: str, total: int) -> str:
 """Set the length of a string to fit within given number of cells."""

 ... 


def chop_cells(
 text: str,
 width: int,
) -> list[str]:
 """Split text into lines such that each line fits within the available (cell) width.

 Args:
 text: The text to fold such that it fits in the given width.
 width: The width available (number of cells).

 Returns:
 A list of strings such that each string in the list has cell width
 less than or equal to the available width.
 """
 ...