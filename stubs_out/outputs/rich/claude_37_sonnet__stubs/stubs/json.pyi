from .highlighter import JSONHighlighter as JSONHighlighter, NullHighlighter as NullHighlighter
from .text import Text as Text
from json import dumps as dumps, loads as loads
from pathlib import Path as Path
from typing import Any, Callable, Optional, Union

class JSON:
    text: Text
    def __init__(self, json: str, indent: Union[None, int, str] = ..., highlight: bool = ..., skip_keys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ...) -> None: ...
    @classmethod
    def from_data(cls, data: Any, indent: Union[None, int, str] = ..., highlight: bool = ..., skip_keys: bool = ..., ensure_ascii: bool = ..., check_circular: bool = ..., allow_nan: bool = ..., default: Optional[Callable[[Any], Any]] = ..., sort_keys: bool = ...) -> JSON: ...
    def __rich__(self) -> Text: ...
