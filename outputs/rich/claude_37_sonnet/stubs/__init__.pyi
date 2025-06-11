from typing import IO, TYPE_CHECKING, Any, Callable, Optional, Union

__all__: list[str]

_console: Optional[Any]
_IMPORT_CWD: str

def get_console() -> Any:
    ...

def reconfigure(*args: Any, **kwargs: Any) -> None:
    ...

def print(*objects: Any, sep: str = ' ', end: str = '\n', file: Optional[IO] = None, flush: bool = False) -> None:
    ...

def print_json(json: Any = None, *, data: Any = None, indent: int = 2, highlight: bool = True, skip_keys: bool = False, ensure_ascii: bool = False, check_circular: bool = True, allow_nan: bool = True, default: Optional[Callable] = None, sort_keys: bool = False) -> None:
    ...

def inspect(obj: Any, *, console: Optional[Any] = None, title: Optional[str] = None, help: bool = False, methods: bool = False, docs: bool = True, private: bool = False, dunder: bool = False, sort: bool = True, all: bool = False, value: bool = True) -> None:
    ...