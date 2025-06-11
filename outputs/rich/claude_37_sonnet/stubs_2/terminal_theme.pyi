from typing import List, Optional, Tuple

from .color_triplet import ColorTriplet
from .palette import Palette

_ColorTuple = Tuple[int, int, int]

class TerminalTheme:
    def __init__(
        self,
        background: _ColorTuple,
        foreground: _ColorTuple,
        normal: List[_ColorTuple],
        bright: Optional[List[_ColorTuple]] = ...,
    ) -> None: ...
    background_color: ColorTriplet
    foreground_color: ColorTriplet
    ansi_colors: Palette

DEFAULT_TERMINAL_THEME: TerminalTheme
MONOKAI: TerminalTheme
DIMMED_MONOKAI: TerminalTheme
NIGHT_OWLISH: TerminalTheme
SVG_EXPORT_THEME: TerminalTheme