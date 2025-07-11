from typing import Iterable, Sequence, Tuple, cast
from rich._win32_console import LegacyWindowsTerm, WindowsCoordinates
from rich.segment import ControlCode, ControlType, Segment

def legacy_windows_render(buffer: Iterable[Segment], term: LegacyWindowsTerm) -> None: ...