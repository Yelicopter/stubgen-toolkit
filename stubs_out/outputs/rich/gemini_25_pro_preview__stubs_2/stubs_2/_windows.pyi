from ctypes import LibraryLoader
from typing import Any, Optional

windll: Optional[LibraryLoader[Any]]

class WindowsConsoleFeatures:
    vt: bool
    truecolor: bool
    def __init__(self, vt, truecolor) -> None: ...

def get_windows_console_features() -> WindowsConsoleFeatures: ...
