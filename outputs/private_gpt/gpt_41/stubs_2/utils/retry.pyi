import logging
from collections.abc import Callable
from typing import Any

from retry_async import retry as retry_untyped

retry_logger: logging.Logger

def retry(
    exceptions: type[Exception] = ...,
    *,
    is_async: bool = ...,
    tries: int = ...,
    delay: int = ...,
    max_delay: int | None = ...,
    backoff: int = ...,
    jitter: int | tuple[float, float] = ...,
    logger: logging.Logger = ...,
) -> Callable[..., Any]: ...