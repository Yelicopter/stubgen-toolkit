import logging
from typing import Any, Callable, Type

def retry(
    exceptions: Type[Exception] = Exception,
    *,
    is_async: bool = False,
    tries: int = -1,
    delay: float = 0,
    max_delay: float | None = None,
    backoff: float = 1,
    jitter: float | tuple[float, float] = 0,
    logger: logging.Logger = logging.getLogger(__name__),
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    ...