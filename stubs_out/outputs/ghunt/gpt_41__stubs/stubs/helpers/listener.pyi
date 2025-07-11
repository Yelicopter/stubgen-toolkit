from ghunt.objects.base import SmartObj
from typing import Any, Type

class DataBridge(SmartObj):
    def __init__(self) -> None: ...
    data: Any

class Server: ...

def run(server_class: Type[Any] = ..., handler_class: Type[Any] = ..., port: int = ...) -> Any: ...
