from typing import Iterable, List, Optional, Tuple

def _to_str(
    size: int,
    suffixes: Iterable[str],
    base: int,
    *,
    precision: Optional[int] = 1,
    separator: Optional[str] = " ",
) -> str: ...

def pick_unit_and_suffix(size: int, suffixes: List[str], base: int) -> Tuple[int, str]: ...

def decimal(
    size: int,
    *,
    precision: Optional[int] = 1,
    separator: Optional[str] = " ",
) -> str: ...