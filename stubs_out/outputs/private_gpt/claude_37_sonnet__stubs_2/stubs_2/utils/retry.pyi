import logging
from collections.abc import Callable as Callable
from typing import Optional, Type, Union

retry_logger: logging.Logger

def retry(exceptions: Type[Exception] | Tuple[Type[Exception], ...] = ..., *, is_async: bool = ..., tries: int = ..., delay: float = ..., max_delay: Optional[float] = ..., backoff: float = ..., jitter: Union[Tuple[float, float], float] = ..., logger: logging.Logger = ...) -> Callable[[Callable], Callable]: ...
