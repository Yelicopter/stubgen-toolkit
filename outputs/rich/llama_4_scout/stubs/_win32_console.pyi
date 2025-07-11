"""Light wrapper around the Win32 Console API - this module should only be imported on Windows

The API that this module wraps is documented at https://docs.microsoft.com/en-us/windows/console/console-functions
"""

import ctypes
import sys
from typing import Any

windll: Any = None
if sys.platform == "win32":
    windll = ctypes.LibraryLoader(ctypes.WinDLL)
else:
    raise ImportError(f"{__name__} can only be imported on Windows")

import time
from ctypes import Structure, byref, wintypes
from typing import IO, NamedTuple, Type, cast

from rich.color import ColorSystem
from rich.style import Style

STDOUT = -11
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 4

COORD = wintypes._COORD


class LegacyWindowsError(Exception):
    pass


class WindowsCoordinates(NamedTuple):
    """Coordinates in the Windows Console API are (y, x), not (x, y).
    This class is intended to prevent that confusion.
    Rows and columns are indexed from 0.
    This class can be used in place of wintypes._COORD in arguments and argtypes.
    """

    # row: int
    # col: int

    @classmethod
    def from_param(cls, value: "WindowsCoordinates") -> wintypes._COORD:
        """Converts a WindowsCoordinates into a wintypes _COORD structure.
        This classmethod is internally called by ctypes to perform the conversion.

        Args:
            value (WindowsCoordinates): The input coordinates to convert.

        Returns:
            wintypes._COORD: The converted coordinates struct.
        """
        ...


class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", wintypes.WORD),
        ("srWindow", wintypes.SMALL_RECT),
        ("dwMaximumWindowSize", COORD),
    ]


class CONSOLE_CURSOR_INFO(ctypes.Structure):
    _fields_ = [("dwSize", wintypes.DWORD), ("bVisible", wintypes.BOOL)]


_GetStdHandle = windll.kernel32.GetStdHandle
_GetStdHandle.argtypes = [
    wintypes.DWORD,
]
_GetStdHandle.restype = wintypes.HANDLE


def GetStdHandle(handle: int = STDOUT) -> wintypes.HANDLE:
    """Retrieves a handle to the specified standard device (standard input, standard output, or standard error).

    Args:
        handle (int): Integer identifier for the handle. Defaults to -11 (stdout).

    Returns:
        wintypes.HANDLE: The handle
    """
    ...


# ... rest of the file remains the same ...