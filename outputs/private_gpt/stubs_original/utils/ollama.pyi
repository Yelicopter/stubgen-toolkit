from _typeshed import Incomplete
from collections.abc import Iterator, Mapping
from ollama import Client as Client
from private_gpt.utils.retry import retry as retry
from typing import Any

logger: Incomplete

def check_connection(client: Client) -> bool: ...
def process_streaming(generator: Iterator[Mapping[str, Any]]) -> None: ...
def pull_model(client: Client, model_name: str, raise_error: bool = ...) -> None: ...
