from .console import Group as Group, RenderableType as RenderableType
from typing import Any, Collection, Optional, Tuple

class Inspect:
    highlighter: Any
    obj: Any
    title: Any
    help: bool
    methods: bool
    docs: bool
    private: bool
    dunder: bool
    sort: bool
    value: bool
    def __init__(self, obj: Any, *, title: Optional[str] = ..., help: bool = ..., methods: bool = ..., docs: bool = ..., private: bool = ..., dunder: bool = ..., sort: bool = ..., all: bool = ..., value: bool = ...) -> None: ...
    def __rich__(self) -> Any: ...

def get_object_types_mro(obj: Any) -> Tuple[Any, ...]: ...
def get_object_types_mro_as_strings(obj: Any) -> list[str]: ...
def is_object_one_of_types(obj: Any, fully_qualified_types_names: Collection[str]) -> bool: ...
