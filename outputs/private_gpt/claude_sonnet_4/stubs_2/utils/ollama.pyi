import logging
from collections import deque
from collections.abc import Iterator, Mapping
from typing import Any, Tuple
from httpx import ConnectError
from tqdm import tqdm
from private_gpt.utils.retry import retry

try:
    from ollama import Client, ResponseError
except ImportError as e:
    raise ImportError(
        "Ollama dependencies not found, install with `poetry install --extras llms-ollama or embeddings-ollama`"
    ) from e

logger: logging.Logger

_MAX_RETRIES: int
_JITTER: Tuple[float, float]

@retry(
    is_async=False,
    exceptions=(ConnectError, ResponseError),
    tries=_MAX_RETRIES,
    jitter=_JITTER,
    logger=logger,
)
def check_connection(client: Client) -> bool: ...

def process_streaming(generator: Iterator[Mapping[str, Any]]) -> None: ...
def pull_model(client: Client, model_name: str, raise_error: bool = True) -> None: ...