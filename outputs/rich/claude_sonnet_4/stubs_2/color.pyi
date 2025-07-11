import re
import sys
from colorsys import rgb_to_hls
from enum import IntEnum
from functools import lru_cache
from typing import TYPE_CHECKING, NamedTuple, Optional, Tuple

from ._palettes import EIGHT_BIT_PALETTE, STANDARD_PALETTE, WINDOWS_PALETTE
from .color_triplet import ColorTriplet
from .repr import Result, rich_repr
from .terminal_theme import DEFAULT_TERMINAL_THEME

if TYPE_CHECKING:
    from .terminal_theme import TerminalTheme

from .text import Text

class ColorSystem(IntEnum):
    STANDARD = 1
    EIGHT_BIT = 2
    TRUECOLOR = 3
    WINDOWS = 4
    
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...

class ColorType(IntEnum):
    DEFAULT = 0
    STANDARD = 1
    EIGHT_BIT = 2
    TRUECOLOR = 3
    WINDOWS = 4
    
    def __repr__(self) -> str: ...

class ColorParseError(Exception): ...

@rich_repr
class Color(NamedTuple):
    name: str
    type: ColorType
    number: Optional[int] = None
    triplet: Optional[ColorTriplet] = None
    
    def __rich__(self) -> Text: ...
    def __rich_repr__(self) -> Result: ...
    
    @property
    def system(self) -> ColorSystem: ...
    
    @property
    def is_system_defined(self) -> bool: ...
    
    @property
    def is_default(self) -> bool: ...
    
    def get_truecolor(
        self,
        theme: Optional["TerminalTheme"] = None,
        foreground: bool = True
    ) -> ColorTriplet: ...
    
    @classmethod
    def from_ansi(cls, number: int) -> "Color": ...
    
    @classmethod
    def from_triplet(cls, triplet: ColorTriplet) -> "Color": ...
    
    @classmethod
    def from_rgb(cls, red: float, green: float, blue: float) -> "Color": ...
    
    @classmethod
    def default(cls) -> "Color": ...
    
    @classmethod
    @lru_cache(maxsize=1024)
    def parse(cls, color: str) -> "Color": ...
    
    @lru_cache(maxsize=1024)
    def get_ansi_codes(self, foreground: bool = True) -> Tuple[str, ...]: ...
    
    @lru_cache(maxsize=1024)
    def downgrade(self, system: ColorSystem) -> "Color": ...

def parse_rgb_hex(hex_color: str) -> ColorTriplet: ...
def blend_rgb(color1: ColorTriplet, color2: ColorTriplet, cross_fade: float = 0.5) -> ColorTriplet: ...