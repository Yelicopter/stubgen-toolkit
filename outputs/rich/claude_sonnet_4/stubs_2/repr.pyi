from typing import Any, Callable, Iterable, Optional, Tuple, Union

Result = Iterable[Union[Any, Tuple[Any], Tuple[str, Any], Tuple[str, Any, Any]]]

def auto(arg: Any) -> Tuple[str, Any, Any]: ...

def rich_repr(cls: Optional[type] = None) -> Union[type, Callable[[type], type]]: ...

class RichReprResult:
    def __init__(
        self,
        class_name: str,
        args: Iterable[Union[Any, Tuple[Optional[str], Any]]],
        kwargs: Iterable[Tuple[str, Any, Any]],
        angular: bool = False
    ) -> None: ...
    
    def __rich_repr__(self) -> Result: ...