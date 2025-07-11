from .color_triplet import ColorTriplet as ColorTriplet
from .palette import Palette as Palette
from typing import List, Optional

class TerminalTheme:
    def __init__(self, background: _ColorTuple, foreground: _ColorTuple, normal: List[_ColorTuple], bright: Optional[List[_ColorTuple]] = ...) -> None: ...
    background_color: ColorTriplet
    foreground_color: ColorTriplet
    ansi_colors: Palette

DEFAULT_TERMINAL_THEME: TerminalTheme
MONOKAI: TerminalTheme
DIMMED_MONOKAI: TerminalTheme
NIGHT_OWLISH: TerminalTheme
SVG_EXPORT_THEME: TerminalTheme
