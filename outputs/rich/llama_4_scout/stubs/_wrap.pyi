from __future__ import annotations

import re
from typing import Iterable

from ._loop import loop_last
from .cells import cell_len, chop_cells

re_word = re.compile(r"\s*\S+\s*")


def words(text: str) -> Iterable[tuple[int, int, str]]:
 """Yields each word from the text as a tuple
 containing (start_index, end_index, word). A "word" in this context may
 include the actual word and any whitespace to the right.
 """
 position = 0
 word_match = re_word.match(text, position)
 while word_match is not None:
  start, end = word_match.span()
 word = word_match.group(0)
 yield start, end, word
 word_match = re_word.match(text, end)


def divide_line(text: str, width: int, fold: bool = True) -> list[int]:
 """Given a string of text, and a width (measured in cells), return a list
 of cell offsets which the string should be split at in order for it to fit
 within the given width.

 Args:
 text: The text to examine.
 width: The available cell width.
 fold: If True, words longer than `width` will be folded onto a new line.

 Returns:
 A list of indices to break the line at.
 """
 ...