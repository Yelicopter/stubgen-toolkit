import sys
from typing import (
    Any,
    Callable,
    Optional,
    Tuple,
    Type,
    Union,
    TypeVar,
    _SpecialForm,
    get_type_hints as _get_type_hints,
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

def is_union(tp: Any) -> bool: ...
NoneType: type
def is_none_type(type_: Any) -> bool: ...
def is_callable_type(type_: Any) -> bool: ...
def is_literal_type(type_: Any) -> bool: ...
def literal_values(type_: Any) -> tuple: ...
def all_literal_values(type_: Any) -> tuple: ...

__all__: tuple[str, ...]