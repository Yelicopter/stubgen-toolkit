from .path import find_closest as find_closest
from pandasai.helpers.telemetry import scarf_analytics as scarf_analytics
from pydantic import BaseModel
from typing import Any, Dict, List

class Log(BaseModel):
    msg: str
    level: int

class Logger:
    def __init__(self, save_logs: bool = ..., verbose: bool = ...) -> None: ...
    def log(self, message: str, level: int = ...) -> None: ...
    @property
    def logs(self) -> List[Dict[str, Any]]: ...
    @property
    def verbose(self) -> bool: ...
    @property
    def save_logs(self) -> bool: ...
