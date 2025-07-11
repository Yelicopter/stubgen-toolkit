from typing import Any, cast, Set, TYPE_CHECKING
from inspect import isclass

if TYPE_CHECKING:
    from rich.console import RenderableType

def is_renderable(check_object: Any) -> bool:
    ...

def rich_cast(renderable: Any) -> "RenderableType":
    ...