from typing import Iterable, List, Literal

class Box:
    _box: str
    ascii: bool
    top_left: str
    top: str
    top_divider: str
    top_right: str
    head_left: str
    head_vertical: str
    head_right: str
    head_row_left: str
    head_row_horizontal: str
    head_row_cross: str
    head_row_right: str
    mid_left: str
    mid_vertical: str
    mid_right: str
    row_left: str
    row_horizontal: str
    row_cross: str
    row_right: str
    foot_row_left: str
    foot_row_horizontal: str
    foot_row_cross: str
    foot_row_right: str
    foot_left: str
    foot_vertical: str
    foot_right: str
    bottom_left: str
    bottom: str
    bottom_divider: str
    bottom_right: str

    def __init__(self, box: str, *, ascii: bool = False) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def substitute(self, options: 'ConsoleOptions', safe: bool = True) -> 'Box':
        ...

    def get_plain_headed_box(self) -> 'Box':
        ...

    def get_top(self, widths: Iterable[int]) -> str:
        ...

    def get_row(self, widths: Iterable[int], level: Literal['head', 'row', 'mid', 'foot'] = 'row', edge: bool = True) -> str:
        ...

    def get_bottom(self, widths: Iterable[int]) -> str:
        ...

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
LEGACY_WINDOWS_SUBSTITUTIONS: dict[Box, Box]
PLAIN_HEADED_SUBSTITUTIONS: dict[Box, Box]