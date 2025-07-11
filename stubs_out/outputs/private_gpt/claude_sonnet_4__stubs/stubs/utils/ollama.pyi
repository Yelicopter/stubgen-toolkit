import logging
from collections import deque as deque
from collections.abc import Iterator, Mapping
from ollama import Client as Client
from tqdm import tqdm as tqdm
from typing import Any

logger: logging.Logger

def check_connection(client: Client) -> bool: ...
def process_streaming(generator: Iterator[Mapping[str, Any]]) -> None: ...
def pull_model(client: Client, model_name: str, raise_error: bool = ...) -> None: ...
