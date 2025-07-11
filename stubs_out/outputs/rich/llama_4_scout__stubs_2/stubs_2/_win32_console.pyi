import ctypes
from _typeshed import Incomplete
from ctypes import Structure, byref as byref, wintypes
from rich.color import ColorSystem as ColorSystem
from rich.style import Style as Style
from typing import Any, NamedTuple

windll: Any
STDOUT: int
ENABLE_VIRTUAL_TERMINAL_PROCESSING: int
COORD: Incomplete

class LegacyWindowsError(Exception): ...

class WindowsCoordinates(NamedTuple):
    @classmethod
    def from_param(cls, value: WindowsCoordinates) -> wintypes._COORD: ...

class CONSOLE_SCREEN_BUFFER_INFO(Structure): ...
class CONSOLE_CURSOR_INFO(ctypes.Structure): ...

def GetStdHandle(handle: int = ...) -> wintypes.HANDLE: ...
