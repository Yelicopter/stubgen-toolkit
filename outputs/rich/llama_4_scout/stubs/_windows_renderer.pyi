from typing import Iterable, Sequence, Tuple, cast

from rich._win32_console import LegacyWindowsTerm, WindowsCoordinates
from rich.segment import ControlCode, ControlType, Segment


def legacy_windows_render(
    buffer: Iterable[Sequence[Segment]], term: LegacyWindowsTerm
) -> None:
    """Makes appropriate Windows Console API calls based on the segments in the buffer.

    Args:
        buffer (Iterable[Segment]): Iterable of Segments to convert to Win32 API calls.
        term (LegacyWindowsTerm): Used to call the Windows Console API.
    """
    ...