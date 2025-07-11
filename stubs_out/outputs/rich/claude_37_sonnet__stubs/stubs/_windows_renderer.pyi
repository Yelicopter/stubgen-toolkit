from rich._win32_console import LegacyWindowsTerm as LegacyWindowsTerm, WindowsCoordinates as WindowsCoordinates
from rich.segment import Segment as Segment
from typing import Sequence

def legacy_windows_render(buffer: Sequence[Segment], term: LegacyWindowsTerm) -> None: ...
