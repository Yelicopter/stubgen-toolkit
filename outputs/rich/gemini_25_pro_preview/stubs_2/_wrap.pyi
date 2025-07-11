from __future__ import annotations

import re
from typing import Iterable, List, Pattern, Tuple

re_word: Pattern[str]

def words(text: str) -> Iterable[Tuple[int, int, str]]: ...
def divide_line(text: str, width: int, fold: bool = True) -> List[int]: ...