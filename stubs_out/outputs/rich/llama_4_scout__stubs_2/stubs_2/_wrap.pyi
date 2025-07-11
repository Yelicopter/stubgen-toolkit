from ._loop import loop_last as loop_last
from .cells import cell_len as cell_len, chop_cells as chop_cells
from _typeshed import Incomplete
from typing import Iterable

re_word: Incomplete

def words(text: str) -> Iterable[tuple[int, int, str]]: ...
def divide_line(text: str, width: int, fold: bool = ...) -> list[int]: ...
