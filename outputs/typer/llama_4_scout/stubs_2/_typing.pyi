from typing import Any, Callable, Optional, Tuple, Type, Union
import sys
from typing_extensions import Annotated, Literal, get_args, get_origin, get_type_hints

def is_union(tp: Type[Any]) -> bool:
    ...

def is_none_type(type_: Type[Any]) -> bool:
    ...

def is_callable_type(type_: Type[Any]) -> bool:
    ...

def is_literal_type(type_: Type[Any]) -> bool:
    ...

def all_literal_values(type_: Type[Any]) -> Tuple[Any, ...]:
    ...