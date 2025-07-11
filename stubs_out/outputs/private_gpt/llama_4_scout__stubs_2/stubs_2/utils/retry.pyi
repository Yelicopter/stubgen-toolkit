import logging
from typing import Any, Callable, Type

def retry(exceptions: Type[Exception] = ..., *, is_async: bool = ..., tries: int = ..., delay: float = ..., max_delay: float | None = ..., backoff: float = ..., jitter: float | tuple[float, float] = ..., logger: logging.Logger = ...) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
