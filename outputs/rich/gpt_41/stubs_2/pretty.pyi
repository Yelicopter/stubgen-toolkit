from typing import Any, Callable, DefaultDict, Deque, Dict, Iterable, List, Optional, Sequence, Set, Tuple, Union

def install(
    console: Optional[Any] = ...,
    overflow: str = ...,
    crop: bool = ...,
    indent_guides: bool = ...,
    max_length: Optional[int] = ...,
    max_string: Optional[int] = ...,
    max_depth: Optional[int] = ...,
    expand_all: bool = ...,
) -> None: ...

class Pretty:
    def __init__(
        self,
        _object: Any,
        highlighter: Optional[Any] = ...,
        *,
        indent_size: int = ...,
        justify: Optional[str] = ...,
        overflow: Optional[str] = ...,
        no_wrap: bool = ...,
        indent_guides: bool = ...,
        max_length: Optional[int] = ...,
        max_string: Optional[int] = ...,
        max_depth: Optional[int] = ...,
        expand_all: bool = ...,
        margin: int = ...,
        insert_line: bool = ...,
    ) -> None: ...
    def __rich_console__(self, console: Any, options: Any) -> Iterable[Any]: ...
    def __rich_measure__(self, console: Any, options: Any) -> Any: ...

def is_expandable(obj: Any) -> bool: ...
def pretty_repr(
    _object: Any,
    *,
    max_width: int = ...,
    indent_size: int = ...,
    max_length: Optional[int] = ...,
    max_string: Optional[int] = ...,
    max_depth: Optional[int] = ...,
    expand_all: bool = ...,
) -> str: ...
def pprint(
    _object: Any,
    *,
    console: Optional[Any] = ...,
    indent_guides: bool = ...,
    max_length: Optional[int] = ...,
    max_string: Optional[int] = ...,
    max_depth: Optional[int] = ...,
    expand_all: bool = ...,
) -> None: ...