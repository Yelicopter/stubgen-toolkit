from typing import Any, Iterable, List, Optional, Sequence, Dict

class Box:
    def __init__(self, box: str, *, ascii: bool = False) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def substitute(self, options: Any, safe: bool = True) -> "Box": ...
    def get_plain_headed_box(self) -> "Box": ...
    def get_top(self, widths: Sequence[int]) -> str: ...
    def get_row(self, widths: Sequence[int], level: str = "row", edge: bool = True) -> str: ...
    def get_bottom(self, widths: Sequence[int]) -> str: ...

ASCII: Box
ASCII2: Box
ASCII_DOUBLE_HEAD: Box
SQUARE: Box
SQUARE_DOUBLE_HEAD: Box
MINIMAL: Box
MINIMAL_HEAVY_HEAD: Box
MINIMAL_DOUBLE_HEAD: Box
SIMPLE: Box
SIMPLE_HEAD: Box
SIMPLE_HEAVY: Box
HORIZONTALS: Box
ROUNDED: Box
HEAVY: Box
HEAVY_EDGE: Box
HEAVY_HEAD: Box
DOUBLE: Box
DOUBLE_EDGE: Box
MARKDOWN: Box
LEGACY_WINDOWS_SUBSTITUTIONS: Dict[str, str]
PLAIN_HEADED_SUBSTITUTIONS: Dict[str, str]