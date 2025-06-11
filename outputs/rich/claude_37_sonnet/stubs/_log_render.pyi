from datetime import datetime
from typing import Iterable, List, Optional, TYPE_CHECKING, Union, Callable
from .text import Text, TextType

if TYPE_CHECKING:
    from .console import Console, ConsoleRenderable, RenderableType

FormatTimeCallable = Callable[[datetime], Text]

class LogRender:
    show_time: bool
    show_level: bool
    show_path: bool
    time_format: Union[str, FormatTimeCallable]
    omit_repeated_times: bool
    level_width: int
    _last_time: Optional[Text]

    def __init__(self, show_time: bool = True, show_level: bool = False, show_path: bool = True, time_format: Union[str, FormatTimeCallable] = '[%x %X]', omit_repeated_times: bool = True, level_width: int = 8) -> None:
        ...

    def __call__(self, console: 'Console', renderables: Iterable['RenderableType'], log_time: Optional[datetime] = None, time_format: Optional[Union[str, FormatTimeCallable]] = None, level: str = '', path: Optional[str] = None, line_no: Optional[int] = None, link_path: Optional[str] = None) -> 'ConsoleRenderable':
        ...