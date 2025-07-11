from collections import deque as deque
from collections.abc import Iterator, Mapping as Mapping
from httpx import ConnectError as ConnectError
from private_gpt.utils.retry import retry as retry
from tqdm import tqdm as tqdm
from typing import Any

def check_connection(client: Any) -> bool: ...
def process_streaming(generator: Iterator[dict[str, Any]]) -> None: ...
def pull_model(client: Any, model_name: str, raise_error: bool = ...) -> None: ...
