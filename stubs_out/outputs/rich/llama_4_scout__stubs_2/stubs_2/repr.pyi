from typing import Any, Iterable, Tuple, TypeVar, Union

T = TypeVar('T')
Result = Iterable[Union[Any, Tuple[Any], Tuple[str, Any], Tuple[str, Any, Any]]]
RichReprResult = Result

class ReprError(Exception): ...

def auto(cls) -> T: ...
def rich_repr(cls) -> T: ...
