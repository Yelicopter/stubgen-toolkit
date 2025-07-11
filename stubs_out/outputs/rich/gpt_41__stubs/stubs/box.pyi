from typing import Any, Sequence

class Box:
    def __init__(self, box: str, *, ascii: bool = ...) -> None: ...
    def substitute(self, options: Any, safe: bool = ...) -> Box: ...
    def get_plain_headed_box(self) -> Box: ...
    def get_top(self, widths: Sequence[int]) -> str: ...
    def get_row(self, widths: Sequence[int], level: str = ..., edge: bool = ...) -> str: ...
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
LEGACY_WINDOWS_SUBSTITUTIONS: dict
PLAIN_HEADED_SUBSTITUTIONS: dict
