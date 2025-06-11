from enum import IntEnum
from typing import NamedTuple, Optional, Tuple, Union
from .color_triplet import ColorTriplet
from .terminal_theme import TerminalTheme

class ColorSystem(IntEnum):
    STANDARD: int
    EIGHT_BIT: int
    TRUECOLOR: int
    WINDOWS: int

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

class ColorType(IntEnum):
    DEFAULT: int
    STANDARD: int
    EIGHT_BIT: int
    TRUECOLOR: int
    WINDOWS: int

    def __repr__(self) -> str:
        ...

ANSI_COLOR_NAMES: dict[str, int]

class ColorParseError(Exception):
    pass

class Color(NamedTuple):
    name: str
    type: ColorType
    number: Optional[int] = None
    triplet: Optional[ColorTriplet] = None

    def __rich__(self) -> Any:
        ...

    @property
    def system(self) -> ColorSystem:
        ...

    @property
    def is_system_defined(self) -> bool:
        ...

    @property
    def is_default(self) -> bool:
        ...

    def get_truecolor(self, theme: Optional[TerminalTheme] = None, foreground: bool = True) -> ColorTriplet:
        ...

    @classmethod
    def from_ansi(cls, number: int) -> 'Color':
        ...

    @classmethod
    def from_triplet(cls, triplet: ColorTriplet) -> 'Color':
        ...

    @classmethod
    def from_rgb(cls, red: int, green: int, blue: int) -> 'Color':
        ...

    @classmethod
    def default(cls) -> 'Color':
        ...

    @classmethod
    def parse(cls, color: str) -> 'Color':
        ...

    def get_ansi_codes(self, foreground: bool = True) -> Tuple[str, ...]:
        ...

    def downgrade(self, system: ColorSystem) -> 'Color':
        ...

def parse_rgb_hex(hex_color: str) -> ColorTriplet:
    ...

def blend_rgb(color1: ColorTriplet, color2: ColorTriplet, cross_fade: float = 0.5) -> ColorTriplet:
    ...