from ._palettes import EIGHT_BIT_PALETTE as EIGHT_BIT_PALETTE, STANDARD_PALETTE as STANDARD_PALETTE, WINDOWS_PALETTE as WINDOWS_PALETTE
from .color_triplet import ColorTriplet as ColorTriplet
from .repr import Result as Result, rich_repr as rich_repr
from .terminal_theme import DEFAULT_TERMINAL_THEME as DEFAULT_TERMINAL_THEME, TerminalTheme as TerminalTheme
from .text import Text as Text
from _typeshed import Incomplete
from colorsys import rgb_to_hls as rgb_to_hls
from enum import IntEnum
from typing import NamedTuple, Optional, Tuple

WINDOWS: Incomplete

class ColorSystem(IntEnum):
    STANDARD: int
    EIGHT_BIT: int
    TRUECOLOR: int
    WINDOWS: int

class ColorType(IntEnum):
    DEFAULT: int
    STANDARD: int
    EIGHT_BIT: int
    TRUECOLOR: int
    WINDOWS: int

ANSI_COLOR_NAMES: Incomplete

class ColorParseError(Exception): ...

RE_COLOR: Incomplete

class Color(NamedTuple):
    def __rich__(self) -> str: ...
    def __rich_repr__(self) -> str: ...
    @property
    def system(self) -> ColorSystem: ...
    @property
    def is_system_defined(self) -> bool: ...
    @property
    def is_default(self) -> bool: ...
    def get_truecolor(self, theme: Optional['TerminalTheme'] = ..., foreground: bool = ...) -> ColorTriplet: ...
    @classmethod
    def from_ansi(cls, number: int) -> Color: ...
    @classmethod
    def from_triplet(cls, triplet: ColorTriplet) -> Color: ...
    @classmethod
    def from_rgb(cls, red: int, green: int, blue: int) -> Color: ...
    @classmethod
    def default(cls) -> Color: ...
    @classmethod
    def parse(cls, color: str) -> Color: ...
    def get_ansi_codes(self, foreground: bool = ...) -> Tuple[str, ...]: ...
    def downgrade(self, system: ColorSystem) -> Color: ...

def parse_rgb_hex(hex_color: str) -> ColorTriplet: ...
def blend_rgb(color1: ColorTriplet, color2: ColorTriplet, cross_fade: float = ...) -> ColorTriplet: ...
