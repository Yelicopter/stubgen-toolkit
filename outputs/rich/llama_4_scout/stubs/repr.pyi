import inspect
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

T = TypeVar("T")

Result = Iterable[Union[Any, Tuple[Any], Tuple[str, Any], Tuple[str, Any, Any]]]
RichReprResult = Result


class ReprError(Exception):
    """An error occurred when attempting to build a repr."""


def auto(cls: T) -> T:
    ...

def rich_repr(cls: T) -> T:
    ...