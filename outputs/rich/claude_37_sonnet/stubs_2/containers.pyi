from itertools import zip_longest
from typing import (
    TYPE_CHECKING,
    Iterable,
    Iterator,
    List,
    Optional,
    TypeVar,
    Union,
    overload,
)

if TYPE_CHECKING:
    from .console import (
        Console,
        ConsoleOptions,
        JustifyMethod,
        OverflowMethod,
        RenderResult,
        RenderableType,
    )
    from .text import Text

from .cells import cell_len
from .measure import Measurement

T = TypeVar("T")

class Renderables:
    _renderables: List["RenderableType"]

    def __init__(
        self, renderables: Optional[Iterable["RenderableType"]] = None
    ) -> None: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "Measurement": ...

    def append(self, renderable: "RenderableType") -> None: ...

    def __iter__(self) -> Iterable["RenderableType"]: ...

class Lines:
    _lines: List["Text"]

    def __init__(self, lines: Iterable["Text"] = ()) -> None: ...

    def __repr__(self) -> str: ...

    def __iter__(self) -> Iterator["Text"]: ...

    @overload
    def __getitem__(self, index: int) -> "Text": ...

    @overload
    def __getitem__(self, index: slice) -> List["Text"]: ...

    def __getitem__(self, index: Union[slice, int]) -> Union["Text", List["Text"]]: ...

    def __setitem__(self, index: int, value: "Text") -> "Lines": ...

    def __len__(self) -> int: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

    def append(self, line: "Text") -> None: ...

    def extend(self, lines: Iterable["Text"]) -> None: ...

    def pop(self, index: int = -1) -> "Text": ...

    def justify(
        self,
        console: "Console",
        width: int,
        justify: "JustifyMethod" = "left",
        overflow: "OverflowMethod" = "fold",
    ) -> None: ...