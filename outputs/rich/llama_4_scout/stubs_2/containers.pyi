from typing import Iterable, Iterator, List, Optional, TypeVar, Union, overload

from .cells import cell_len
from .measure import Measurement

T = TypeVar("T")

class RenderableType:
    ...

class Console:
    ...

class ConsoleOptions:
    ...

class RenderResult:
    ...

class Renderables:
    def __init__(self, renderables: Optional[Iterable[RenderableType]] = None) -> None:
        ...

    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult":
        ...

    def __rich_measure__(self, console: "Console", options: "ConsoleOptions") -> "Measurement":
        ...

    def append(self, renderable: RenderableType) -> None:
        ...

    def __iter__(self) -> Iterator[RenderableType]:
        ...

class Lines:
    def __init__(self, lines: Iterable["Text"] = ()) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __iter__(self) -> Iterator["Text"]:
        ...

    @overload
    def __getitem__(self, index: int) -> "Text":
        ...

    @overload
    def __getitem__(self, index: slice) -> "Lines":
        ...

    def __getitem__(self, index: Union[int, slice]) -> Union["Text", "Lines"]:
        ...

    def __setitem__(self, index: int, value: "Text") -> "Lines":
        ...

    def __len__(self) -> int:
        ...

    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult":
        ...

    def append(self, line: "Text") -> None:
        ...

    def extend(self, lines: Iterable["Text"]) -> None:
        ...

    def pop(self, index: int = -1) -> "Text":
        ...

    def justify(
        self,
        console: "Console",
        width: int,
        justify: str = "left",
        overflow: str = "fold",
    ) -> None:
        ...