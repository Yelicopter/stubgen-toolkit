from datetime import datetime
from typing import Iterable, List, Optional, TYPE_CHECKING, Union, Callable


from .text import Text, TextType

if TYPE_CHECKING:
    from .console import Console, ConsoleRenderable, RenderableType
    from .table import Table

FormatTimeCallable = Callable[[datetime], Text]


class LogRender:
    def __init__(
        self,
        show_time: bool = True,
        show_level: bool = False,
        show_path: bool = True,
        time_format: str = "[%x %X]",
        omit_repeated_times: bool = True,
        level_width: int = 8,
    ) -> None:
        ...

    def __call__(
        self,
        console: "Console",
        renderables: Iterable[RenderableType],
        log_time: Optional[datetime] = None,
        time_format: Optional[str] = None,
        level: str = "",
        path: Optional[str] = None,
        line_no: Optional[int] = None,
        link_path: Optional[str] = None,
    ) -> "Table":
        ...