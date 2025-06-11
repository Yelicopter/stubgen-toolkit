import ctypes
import sys
from typing import Any, IO, NamedTuple, Type, cast, List
from ctypes import Structure, byref, wintypes
from rich.color import ColorSystem
from rich.style import Style

windll: Any
STDOUT: int
ENABLE_VIRTUAL_TERMINAL_PROCESSING: int
COORD: Any

class LegacyWindowsError(Exception):
    pass

class WindowsCoordinates(NamedTuple):
    row: int
    col: int
    
    @classmethod
    def from_param(cls, value: 'WindowsCoordinates') -> COORD:
        ...

class CONSOLE_SCREEN_BUFFER_INFO(Structure): ...

class CONSOLE_CURSOR_INFO(ctypes.Structure): ...

def GetStdHandle(handle: int = STDOUT) -> wintypes.HANDLE:
    ...

def GetConsoleMode(std_handle: wintypes.HANDLE) -> int:
    ...

def FillConsoleOutputCharacter(std_handle: wintypes.HANDLE, char: str, length: int, start: WindowsCoordinates) -> int:
    ...

def FillConsoleOutputAttribute(std_handle: wintypes.HANDLE, attributes: int, length: int, start: WindowsCoordinates) -> int:
    ...

def SetConsoleTextAttribute(std_handle: wintypes.HANDLE, attributes: int) -> bool:
    ...

def GetConsoleScreenBufferInfo(std_handle: wintypes.HANDLE) -> CONSOLE_SCREEN_BUFFER_INFO:
    ...

def SetConsoleCursorPosition(std_handle: wintypes.HANDLE, coords: WindowsCoordinates) -> bool:
    ...

def GetConsoleCursorInfo(std_handle: wintypes.HANDLE, cursor_info: CONSOLE_CURSOR_INFO) -> bool:
    ...

def SetConsoleCursorInfo(std_handle: wintypes.HANDLE, cursor_info: CONSOLE_CURSOR_INFO) -> bool:
    ...

def SetConsoleTitle(title: str) -> bool:
    ...

class LegacyWindowsTerm:
    BRIGHT_BIT: int
    ANSI_TO_WINDOWS: List[int]
    _handle: wintypes.HANDLE
    _default_text: int
    _default_fore: int
    _default_back: int
    _default_attrs: int
    _file: IO[Any]
    write: Any
    flush: Any

    def __init__(self, file: IO[Any]) -> None:
        ...

    @property
    def cursor_position(self) -> WindowsCoordinates:
        ...

    @property
    def screen_size(self) -> WindowsCoordinates:
        ...

    def write_text(self, text: str) -> None:
        ...

    def write_styled(self, text: str, style: Style) -> None:
        ...

    def move_cursor_to(self, new_position: WindowsCoordinates) -> None:
        ...

    def erase_line(self) -> None:
        ...

    def erase_end_of_line(self) -> None:
        ...

    def erase_start_of_line(self) -> None:
        ...

    def move_cursor_up(self) -> None:
        ...

    def move_cursor_down(self) -> None:
        ...

    def move_cursor_forward(self) -> None:
        ...

    def move_cursor_to_column(self, column: int) -> None:
        ...

    def move_cursor_backward(self) -> None:
        ...

    def hide_cursor(self) -> None:
        ...

    def show_cursor(self) -> None:
        ...

    def set_title(self, title: str) -> None:
        ...

    def _get_cursor_size(self) -> int:
        ...