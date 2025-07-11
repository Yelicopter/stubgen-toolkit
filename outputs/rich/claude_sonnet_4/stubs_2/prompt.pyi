from typing import Any, List, Optional, Union

from .console import Console
from .text import Text, TextType

class PromptError(Exception): ...
class InvalidResponse(PromptError): ...

class PromptBase:
    def __init__(
        self,
        prompt: TextType = "",
        *,
        console: Optional[Console] = None,
        password: bool = False,
        choices: Optional[List[str]] = None,
        show_default: bool = True,
        show_choices: bool = True
    ) -> None: ...
    
    def __call__(self, *, stream: Optional[Any] = None) -> Any: ...

class Prompt(PromptBase):
    response_type: type = str
    
    def process_response(self, value: str) -> Any: ...

class IntPrompt(Prompt):
    response_type: type = int
    
    def process_response(self, value: str) -> int: ...

class FloatPrompt(Prompt):
    response_type: type = float
    
    def process_response(self, value: str) -> float: ...

class Confirm(PromptBase):
    response_type: type = bool
    
    def __init__(
        self,
        prompt: TextType = "",
        *,
        console: Optional[Console] = None,
        password: bool = False,
        choices: Optional[List[str]] = None,
        show_default: bool = True,
        show_choices: bool = True,
        default: bool = False
    ) -> None: ...
    
    def process_response(self, value: str) -> bool: ...