import sys
from typing import (
    Any,
    Callable,
    Optional,
    Tuple,
    Type,
    Union,
)

if sys.version_info >= (3, 9):
    from typing import Annotated, Literal, get_args, get_origin, get_type_hints
else:
    from typing_extensions import (
        Annotated,
        Literal,
        get_args,
        get_origin,
        get_type_hints,
    )

if sys.version_info < (3, 10):
    def is_union(tp: Optional[Type[Any]]) -> bool: ...
else:
    import types
    def is_union(tp: Optional[Type[Any]]) -> bool: ...

__all__: Tuple[str, ...]

NoneType: Type[None]

def is_none_type(type_: Type[Any]) -> bool: ...
def is_callable_type(type_: Type[Any]) -> bool: ...
def is_literal_type(type_: Type[Any]) -> bool: ...
def literal_values(type_: Type[Any]) -> Tuple[Any, ...]: ...
def all_literal_values(type_: Type[Any]) -> Tuple[Any, ...]: ...