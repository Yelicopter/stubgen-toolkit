import logging
from collections.abc import Callable
from typing import Any, Optional, Type, TypeVar, Union

from retry_async import retry as retry_untyped

retry_logger: logging.Logger

def retry(
    exceptions: Type[Exception] | Tuple[Type[Exception], ...] = Exception,
    *,
    is_async: bool = False,
    tries: int = -1,
    delay: float = 0,
    max_delay: Optional[float] = None,
    backoff: float = 1,
    jitter: Union[Tuple[float, float], float] = 0,
    logger: logging.Logger = retry_logger,
) -> Callable[[Callable], Callable]: ...