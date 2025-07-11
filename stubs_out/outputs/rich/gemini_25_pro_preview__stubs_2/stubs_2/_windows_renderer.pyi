from rich._win32_console import LegacyWindowsTerm as LegacyWindowsTerm
from rich.segment import ControlCode as ControlCode
from rich.style import Style as Style
from typing import Iterable, Optional, Sequence, Tuple

def legacy_windows_render(buffer: Iterable[Tuple[str, Optional[Style], Optional[Sequence[ControlCode]]]], term: LegacyWindowsTerm) -> None: ...
