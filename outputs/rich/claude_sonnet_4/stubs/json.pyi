from typing import Any, Dict, IO, Optional, Union

from .highlighter import JSONHighlighter
from .jupyter import JupyterMixin
from .text import Text

class JSON(JupyterMixin):
    def __init__(
        self,
        json: str,
        indent: Union[None, int, str] = 2,
        highlight: bool = True,
        skip_keys: bool = False,
        ensure_ascii: bool = False,
        check_circular: bool = True,
        allow_nan: bool = True,
        default: Optional[Any] = None,
        sort_keys: bool = False
    ) -> None: ...
    
    @classmethod
    def from_data(
        cls,
        data: Any,
        indent: Union[None, int, str] = 2,
        highlight: bool = True,
        skip_keys: bool = False,
        ensure_ascii: bool = False,
        check_circular: bool = True,
        allow_nan: bool = True,
        default: Optional[Any] = None,
        sort_keys: bool = False
    ) -> "JSON": ...
    
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...