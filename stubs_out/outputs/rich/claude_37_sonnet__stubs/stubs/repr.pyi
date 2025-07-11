from functools import partial as partial
from typing import Any, Callable, Iterable, Tuple, Type, TypeVar, Union, overload

T = TypeVar('T')
Result = Iterable[Union[Any, Tuple[Any], Tuple[str, Any], Tuple[str, Any, Any]]]
RichReprResult = Result

class ReprError(Exception): ...


@overload
def auto(cls) -> Type[T]: ...
@overload
def auto(*, angular: bool = ...) -> Callable[[Type[T]], Type[T]]: ...
@overload
def rich_repr(cls) -> Type[T]: ...
@overload
def rich_repr(*, angular: bool = ...) -> Callable[[Type[T]], Type[T]]: ...
