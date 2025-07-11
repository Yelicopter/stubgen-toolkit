from typing import TYPE_CHECKING, Any, Iterable, Union, cast

from .console import Console

if TYPE_CHECKING:
    from .console import ConsoleRenderable

def is_renderable(check_object: Any) -> bool: ...
def rich_cast(renderable: Union[str, "ConsoleRenderable"]) -> Union[str, "ConsoleRenderable"]: ...