from collections.abc import Iterator, Mapping
from typing import Any

try:
    from ollama import Client
except ImportError:
    Client = Any

def check_connection(client: Client) -> bool: ...
def process_streaming(generator: Iterator[Mapping[str, Any]]) -> None: ...
def pull_model(client: Client, model_name: str, raise_error: bool = ...) -> None: ...