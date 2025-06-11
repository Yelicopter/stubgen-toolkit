from typing import Iterable, Sequence, Tuple, cast
from rich._win32_console import LegacyWindowsTerm, WindowsCoordinates
from rich.segment import Segment

def legacy_windows_render(buffer: Sequence[Segment], term: LegacyWindowsTerm) -> None:
    ...