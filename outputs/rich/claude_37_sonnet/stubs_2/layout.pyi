from abc import ABC, abstractmethod
from itertools import islice
from operator import itemgetter
from threading import RLock
from typing import (
    TYPE_CHECKING,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from ._ratio import ratio_resolve
from .align import Align
from .console import Console, ConsoleOptions, RenderableType, RenderResult
from .highlighter import ReprHighlighter
from .panel import Panel
from .pretty import Pretty
from .region import Region
from .repr import Result, rich_repr
from .segment import Segment
from .style import StyleType

if TYPE_CHECKING:
    from rich.tree import Tree

class LayoutRender(NamedTuple):
    region: Region
    render: List[List[Segment]]

RegionMap = Dict["Layout", Region]
RenderMap = Dict["Layout", LayoutRender]

class LayoutError(Exception): ...

class NoSplitter(LayoutError): ...

class _Placeholder:
    highlighter: ReprHighlighter

    def __init__(self, layout: "Layout", style: StyleType = "") -> None: ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...

class Splitter(ABC):
    name: str

    @abstractmethod
    def get_tree_icon(self) -> str: ...

    @abstractmethod
    def divide(
        self, children: Sequence["Layout"], region: Region
    ) -> Iterable[Tuple["Layout", Region]]: ...

class RowSplitter(Splitter):
    name: str

    def get_tree_icon(self) -> str: ...

    def divide(
        self, children: Sequence["Layout"], region: Region
    ) -> Iterable[Tuple["Layout", Region]]: ...

class ColumnSplitter(Splitter):
    name: str

    def get_tree_icon(self) -> str: ...

    def divide(
        self, children: Sequence["Layout"], region: Region
    ) -> Iterable[Tuple["Layout", Region]]: ...

@rich_repr
class Layout:
    splitters: Dict[str, type]

    def __init__(
        self,
        renderable: Optional[RenderableType] = None,
        *,
        name: Optional[str] = None,
        size: Optional[int] = None,
        minimum_size: int = 1,
        ratio: int = 1,
        visible: bool = True,
    ) -> None: ...

    def __rich_repr__(self) -> Result: ...

    @property
    def renderable(self) -> RenderableType: ...

    @property
    def children(self) -> List["Layout"]: ...

    @property
    def map(self) -> RenderMap: ...

    def get(self, name: str) -> Optional["Layout"]: ...

    def __getitem__(self, name: str) -> "Layout": ...

    @property
    def tree(self) -> "Tree": ...

    def split(
        self,
        *layouts: Union["Layout", RenderableType],
        splitter: Union[Splitter, str] = "column",
    ) -> None: ...

    def add_split(self, *layouts: Union["Layout", RenderableType]) -> None: ...

    def split_row(self, *layouts: Union["Layout", RenderableType]) -> None: ...

    def split_column(self, *layouts: Union["Layout", RenderableType]) -> None: ...

    def unsplit(self) -> None: ...

    def update(self, renderable: RenderableType) -> None: ...

    def refresh_screen(self, console: "Console", layout_name: str) -> None: ...

    def _make_region_map(self, width: int, height: int) -> RegionMap: ...

    def render(self, console: Console, options: ConsoleOptions) -> RenderMap: ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...