from typing import Iterable, List, Tuple

def words(text: str) -> Iterable[Tuple[int, int, str]]:
    ...

def divide_line(text: str, width: int, fold: bool = True) -> List[int]:
    ...