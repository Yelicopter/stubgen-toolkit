from __future__ import annotations

from typing import Iterable, Optional, Sequence, Tuple

from rich._win32_console import LegacyWindowsTerm
from rich.segment import ControlCode
from rich.style import Style

def legacy_windows_render(buffer: Iterable[Tuple[str, Optional[Style], Optional[Sequence[ControlCode]]]], term: LegacyWindowsTerm) -> None: ...