from enum import IntEnum
from rich.text import Text as Text
from typing import Any, Dict, NamedTuple, Optional, Pattern, Tuple

WINDOWS: bool

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

ANSI_COLOR_NAMES: Dict[str, int]

class ColorParseError(Exception): ...

RE_COLOR: Pattern[str]

class ColorTriplet(NamedTuple):
    red: int
    green: int
    blue: int

class TerminalTheme:
    def __init__(self) -> None: ...

class Result:
    def __init__(self, *args: Any) -> None: ...

class Color(NamedTuple):
    name: str
    type: ColorType
    number: Optional[int]
    triplet: Optional[ColorTriplet]
    def __rich__(self) -> Text: ...
    def __rich_repr__(self) -> Result: ...
    @property
    def system(self) -> ColorSystem: ...
    @property
    def is_system_defined(self) -> bool: ...
    @property
    def is_default(self) -> bool: ...
    def get_truecolor(self, theme: Optional[TerminalTheme] = ..., foreground: bool = ...) -> ColorTriplet: ...
    @classmethod
    def from_ansi(cls, number: int) -> Color: ...
    @classmethod
    def from_triplet(cls, triplet: ColorTriplet) -> Color: ...
    @classmethod
    def from_rgb(cls, red: float, green: float, blue: float) -> Color: ...
    @classmethod
    def default(cls) -> Color: ...
    @classmethod
    def parse(cls, color: str) -> Color: ...
    def get_ansi_codes(self, foreground: bool = ...) -> Tuple[str, ...]: ...
    def downgrade(self, system: ColorSystem) -> Color: ...

def parse_rgb_hex(hex_color: str) -> ColorTriplet: ...
def blend_rgb(color1: ColorTriplet, color2: ColorTriplet, cross_fade: float = ...) -> ColorTriplet: ...
