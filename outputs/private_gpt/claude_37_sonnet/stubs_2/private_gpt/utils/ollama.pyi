import logging
from collections.abc import Iterator, Mapping
from typing import Any, Optional

from httpx import ConnectError
from tqdm import tqdm

from private_gpt.utils.retry import retry

logger: logging.Logger

_MAX_RETRIES: int
_JITTER: Tuple[float, float]

def check_connection(client: Any) -> bool: ...
def process_streaming(generator: Iterator[Mapping[str, Any]]) -> None: ...
def pull_model(client: Any, model_name: str, raise_error: bool = True) -> None: ...