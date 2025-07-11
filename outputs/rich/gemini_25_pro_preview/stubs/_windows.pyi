from __future__ import annotations

from ctypes import LibraryLoader
from dataclasses import dataclass
from typing import Optional

windll: Optional[LibraryLoader]

@dataclass
class WindowsConsoleFeatures:
    vt: bool
    truecolor: bool

def get_windows_console_features() -> WindowsConsoleFeatures: ...