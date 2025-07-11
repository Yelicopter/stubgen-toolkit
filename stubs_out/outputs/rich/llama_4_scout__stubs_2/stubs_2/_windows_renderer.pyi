from rich._win32_console import LegacyWindowsTerm as LegacyWindowsTerm, WindowsCoordinates as WindowsCoordinates
from rich.segment import ControlCode as ControlCode, ControlType as ControlType, Segment as Segment
from typing import Iterable, Sequence

def legacy_windows_render(buffer: Iterable[Sequence[Segment]], term: LegacyWindowsTerm) -> None: ...
