from typing import Iterable, List, Optional, Tuple


def _to_str(
    size: int,
    suffixes: Iterable[str],
    base: int,
    *,
    precision: int = 1,
    separator: str = " ",
) -> str:
    ...

def pick_unit_and_suffix(size: int, suffixes: Iterable[str], base: int) -> Tuple[int, str]:
    ...

def decimal(
    size: int,
    *,
    precision: int = 1,
    separator: str = " ",
) -> str:
    ...