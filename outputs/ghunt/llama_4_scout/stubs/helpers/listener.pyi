from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any

class DataBridge:
    def __init__(self) -> None:
        ...

class Server(BaseHTTPRequestHandler):
    ...

def run(server_class: Any = HTTPServer, handler_class: Any = Server, port: int = 60067) -> Any:
    ...