import logging
from collections.abc import Callable as Callable
from private_gpt.utils.typing import T as T
from typing import Type, Union

retry_logger: logging.Logger

def retry(exceptions: Union[Type[Exception], tuple[Type[Exception], ...]] = ..., *, is_async: bool = ..., tries: int = ..., delay: Union[int, float] = ..., max_delay: Union[int, float, None] = ..., backoff: Union[int, float] = ..., jitter: Union[int, float, tuple[Union[int, float], Union[int, float]]] = ..., logger: logging.Logger | None = ...) -> Callable[[Callable[..., T]], Callable[..., T]]: ...
