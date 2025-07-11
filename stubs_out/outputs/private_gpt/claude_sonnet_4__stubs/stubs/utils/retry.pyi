import logging
from collections.abc import Callable as Callable
from typing import Any, Optional, Tuple, Union

retry_logger: logging.Logger

def retry(exceptions: Union[type, Tuple[type, ...]] = ..., *, is_async: bool = ..., tries: int = ..., delay: float = ..., max_delay: Optional[float] = ..., backoff: float = ..., jitter: Union[float, Tuple[float, float]] = ..., logger: logging.Logger = ...) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
