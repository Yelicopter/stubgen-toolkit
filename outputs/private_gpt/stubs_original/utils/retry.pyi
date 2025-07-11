import logging
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from typing import Any

retry_logger: Incomplete

def retry(exceptions: Any = ..., *, is_async: bool = ..., tries: int = ..., delay: float = ..., max_delay: float | None = ..., backoff: float = ..., jitter: float | tuple[float, float] = ..., logger: logging.Logger = ...) -> Callable[..., Any]: ...
