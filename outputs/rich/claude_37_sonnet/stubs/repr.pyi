import inspect
from functools import partial
from typing import Any, Callable, Iterable, List, Optional, Tuple, Type, TypeVar, Union, overload

T = TypeVar("T")

Result = Iterable[Union[Any, Tuple[Any], Tuple[str, Any], Tuple[str, Any, Any]]]
RichReprResult = Result

class ReprError(Exception): ...

@overload
def auto(cls: Optional[Type[T]]) -> Type[T]: ...
@overload
def auto(*, angular: bool = ...) -> Callable[[Type[T]], Type[T]]: ...

@overload
def rich_repr(cls: Optional[Type[T]]) -> Type[T]: ...
@overload
def rich_repr(*, angular: bool = ...) -> Callable[[Type[T]], Type[T]]: ...