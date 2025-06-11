import io
from typing import IO, TYPE_CHECKING, Any, List

from .ansi import AnsiDecoder
from .text import Text

if TYPE_CHECKING:
    from .console import Console

class FileProxy(io.TextIOBase):
    def __init__(self, console: "Console", file: IO[str]) -> None: ...

    @property
    def rich_proxied_file(self) -> IO[str]: ...

    def __getattr__(self, name: str) -> Any: ...

    def write(self, text: str) -> int: ...

    def flush(self) -> None: ...

    def fileno(self) -> int: ...