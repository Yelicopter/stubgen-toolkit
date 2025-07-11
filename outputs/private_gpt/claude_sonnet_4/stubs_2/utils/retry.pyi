import logging
from collections.abc import Callable
from typing import Any, Union, Tuple, Optional
from retry_async import retry as retry_untyped

retry_logger: logging.Logger

def retry(
    exceptions: Union[type, Tuple[type, ...]] = Exception,
    *,
    is_async: bool = False,
    tries: int = -1,
    delay: float = 0,
    max_delay: Optional[float] = None,
    backoff: float = 1,
    jitter: Union[float, Tuple[float, float]] = 0,
    logger: logging.Logger = retry_logger,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...