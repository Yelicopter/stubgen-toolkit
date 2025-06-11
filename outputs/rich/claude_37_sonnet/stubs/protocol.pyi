from typing import Any, cast, Set, TYPE_CHECKING

from rich.console import RenderableType

_GIBBERISH: str

def is_renderable(check_object: Any) -> bool: ...
def rich_cast(renderable: object) -> RenderableType: ...