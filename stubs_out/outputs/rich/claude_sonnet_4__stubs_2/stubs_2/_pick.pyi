from typing import Optional, TypeVar

T = TypeVar('T')

def pick_bool(*values: Optional[bool]) -> bool: ...
