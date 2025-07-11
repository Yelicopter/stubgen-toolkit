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
    """An individual layout render."""

    region: Region
    render: List[List[Segment]]


RegionMap = Dict["Layout", Region]
RenderMap = Dict["Layout", LayoutRender]


class LayoutError(Exception):
    """Layout related error."""


class NoSplitter(LayoutError):
    """Requested splitter does not exist."""


class _Placeholder:
    """An internal renderable used as a Layout placeholder."""

    highlighter: ReprHighlighter

    def __init__(self, layout: "Layout", style: StyleType = ""):
        self.layout = layout
        self.style = style

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> Iterable[Segment]:
        ...


class Splitter(ABC):
    """Base class for a splitter."""

    name: str = ""

    @abstractmethod
    def get_tree_icon(self) -> str:
        """Get the icon (emoji) used in layout.tree"""

    @abstractmethod
    def divide(
        self, children: Sequence["Layout"], region: Region
    ) -> Iterable[Tuple["Layout", Region]]:
        """Divide a region amongst several child layouts.

        Args:
            children (Sequence(Layout)): A number of child layouts.
            region (Region): A rectangular region to divide.
        """


class RowSplitter(Splitter):
    """Split a layout region in to rows."""

    name = "row"

    def get_tree_icon(self) -> str:
        return "[layout.tree.row]⬌"

    def divide(
        self, children: Sequence["Layout"], region: Region
    ) -> Iterable[Tuple["Layout", Region]]:
        ...


class ColumnSplitter(Splitter):
    """Split a layout region in to columns."""

    name = "column"

    def get_tree_icon(self) -> str:
        return "[layout.tree.column]⬍"

    def divide(
        self, children: Sequence["Layout"], region: Region
    ) -> Iterable[Tuple["Layout", Region]]:
        ...


@rich_repr
class Layout:
    """A renderable to divide a fixed height in to rows or columns.

    Args:
        renderable (RenderableType, optional): Renderable content, or None for placeholder. Defaults to None.
        name (str, optional): Optional identifier for Layout. Defaults to None.
        size (int, optional): Optional fixed size of layout. Defaults to None.
        minimum_size (int, optional): Minimum size of layout. Defaults to 1.
        ratio (int, optional): Optional ratio for flexible layout. Defaults to 1.
        visible (bool, optional): Visibility of layout. Defaults to True.
    """

    splitters: Dict[str, Splitter] = {}

    def __init__(
        self,
        renderable: RenderableType = None,
        *,
        name: Optional[str] = None,
        size: Optional[int] = None,
        minimum_size: int = 1,
        ratio: int = 1,
        visible: bool = True,
    ):
        ...

    def __rich_repr__(self) -> Result:
        ...

    @property
    def renderable(self) -> RenderableType:
        """Layout renderable."""
        ...

    @property
    def children(self) -> List["Layout"]:
        """Gets (visible) layout children."""
        ...

    @property
    def map(self) -> RenderMap:
        """Get a map of the last render."""
        ...

    def get(self, name: str) -> Optional["Layout"]:
        """Get a named layout, or None if it doesn't exist.

        Args:
            name (str): Name of layout.

        Returns:
            Optional[Layout]: Layout instance or None if no layout was found.
        """
        ...

    def __getitem__(self, name: str) -> "Layout":
        ...

    @property
    def tree(self) -> "Tree":
        """Get a tree renderable to show layout structure."""
        ...

    def split(
        self, *layouts: "Layout", splitter: Union[Splitter, str] = "column"
    ) -> None:
        """Split the layout in to multiple sub-layouts.

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
            splitter (Union[Splitter, str]): Splitter instance or name of splitter.
        """
        ...

    def add_split(self, *layouts: Union["Layout", RenderableType]) -> None:
        """Add a new layout(s) to existing split.

        Args:
            *layouts (Union[Layout, RenderableType]): Positional arguments should be renderables or (sub) Layout instances.

        """
        ...

    def split_row(self, *layouts: "Layout") -> None:
        """Split the layout in to a row (layouts side by side).

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
        """
        ...

    def split_column(self, *layouts: "Layout") -> None:
        """Split the layout in to a column (layouts stacked on top of each other).

        Args:
            *layouts (Layout): Positional arguments should be (sub) Layout instances.
        """
        ...

    def unsplit(self) -> None:
        """Reset splits to initial state."""
        ...

    def update(self, renderable: RenderableType) -> None:
        """Update renderable.

        Args:
            renderable (RenderableType): New renderable object.
        """
        ...

    def refresh_screen(self, console: Console, layout_name: str) -> None:
        """Refresh a sub-layout.

        Args:
            console (Console): Console instance where Layout is to be rendered.
            layout_name (str): Name of layout.
        """
        ...

    def _make_region_map(self, width: int, height: int) -> RegionMap:
        """Create a dict that maps layout on to Region."""
        ...

    def render(self, console: Console, options: ConsoleOptions) -> RenderMap:
        """Render the sub_layouts.

        Args:
            console (Console): Console instance.
            options (ConsoleOptions): Console options.

        Returns:
            RenderMap: A dict that maps Layout on to a tuple of Region, lines
        """
        ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> Iterable[Segment]:
        ...