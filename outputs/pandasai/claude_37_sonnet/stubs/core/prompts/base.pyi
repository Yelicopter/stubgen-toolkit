import os
import re
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional

from jinja2 import Environment, FileSystemLoader

class BasePrompt:
    template: Optional[str] = None
    template_path: Optional[str] = None
    props: Dict[str, Any]
    prompt: Any
    _resolved_prompt: Optional[str]
    
    def __init__(self, **kwargs) -> None: ...
    
    def render(self) -> str: ...
    
    def to_string(self) -> str: ...
    
    def __str__(self) -> str: ...
    
    def validate(self, output: str) -> bool: ...
    
    def to_json(self) -> Dict[str, Any]: ...

class AbstractPrompt(ABC):
    @abstractmethod
    def get_prompt(self) -> str: ...

__all__: List[str]