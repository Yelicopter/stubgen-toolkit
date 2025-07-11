import logging
from collections import deque
from collections.abc import Iterator, Mapping
from typing import Any

from httpx import ConnectError
from tqdm import tqdm

from private_gpt.utils.retry import retry

def check_connection(client: Any) -> bool: ...
def process_streaming(generator: Iterator[dict[str, Any]]) -> None: ...
def pull_model(client: Any, model_name: str, raise_error: bool = True) -> None: ...