from typing import Any, Collection, Iterable, Optional, Tuple, Type, Union
from .console import Group, RenderableType

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

    def __init__(self, obj: Any, *, title: Optional[str] = None, help: bool = False, methods: bool = False, docs: bool = True, private: bool = False, dunder: bool = False, sort: bool = True, all: bool = True, value: bool = True) -> None:
        ...

    def _make_title(self, obj: Any) -> Any:
        ...

    def __rich__(self) -> Any:
        ...

    def _get_signature(self, name: str, obj: Any) -> Optional[Any]:
        ...

    def _render(self) -> Iterable[Any]:
        ...

    def _get_formatted_doc(self, object_: Any) -> Optional[str]:
        ...

def get_object_types_mro(obj: Any) -> Tuple[Any, ...]:
    ...

def get_object_types_mro_as_strings(obj: Any) -> list[str]:
    ...

def is_object_one_of_types(obj: Any, fully_qualified_types_names: Collection[str]) -> bool:
    ...