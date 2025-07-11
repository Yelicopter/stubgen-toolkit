from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .highlighter import JSONHighlighter as JSONHighlighter
from .jupyter import JupyterMixin as JupyterMixin
from .text import Text as Text
from typing import Any, Optional, Union

class JSON(JupyterMixin):
    def __init__(self, json: str, indent: Union[None, int, str] = ..., highlight: bool = ..., skip_keys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., default: Optional[Any] = ..., sort_keys: bool = ...) -> None: ...
    @classmethod
    def from_data(cls, data: Any, indent: Union[None, int, str] = ..., highlight: bool = ..., skip_keys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., default: Optional[Any] = ..., sort_keys: bool = ...) -> JSON: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
