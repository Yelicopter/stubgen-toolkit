from enum import Enum
from pydantic import BaseModel
from typing import Any, Callable, Dict, Set, Type, TypeVar, Union

DecoratedCallable = TypeVar('DecoratedCallable', bound=Callable[..., Any])
UnionType: Type[Any]
ModelNameMap = Dict[Union[Type[BaseModel], Type[Enum]], str]
IncEx = Union[Set[int], Set[str], Dict[int, Any], Dict[str, Any]]
