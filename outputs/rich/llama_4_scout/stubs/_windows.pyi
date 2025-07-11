import sys
from dataclasses import dataclass


@dataclass
class WindowsConsoleFeatures:
    """Windows features available."""

    vt: bool = False
    """The console supports VT codes."""
    truecolor: bool = False
    """The console supports truecolor."""


try:
    import ctypes
    from ctypes import LibraryLoader

    if sys.platform == "win32":
        windll = LibraryLoader(ctypes.WinDLL)
    else:
        windll = None
        raise ImportError("Not windows")

    from rich._win32_console import (
        ENABLE_VIRTUAL_TERMINAL_PROCESSING,
        GetConsoleMode,
        GetStdHandle,
        LegacyWindowsError,
    )

except (AttributeError, ImportError, ValueError):
    # Fallback if we can't load the Windows DLL
    def get_windows_console_features() -> WindowsConsoleFeatures:
        ...

else:

    def get_windows_console_features() -> WindowsConsoleFeatures:
        """Get windows console features.

        Returns:
            WindowsConsoleFeatures: An instance of WindowsConsoleFeatures.
        """
        ...