import sys
from typing import TYPE_CHECKING, Iterable, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal  # pragma: no cover


from ._loop import loop_last

if TYPE_CHECKING:
    from rich.console import ConsoleOptions


class Box:
    """Defines characters to render boxes.

    ┌─┬┐ top
    │ ││ head
    ├─┼┤ head_row
    │ ││ mid
    ├─┼┤ row
    ├─┼┤ foot_row
    │ ││ foot
    └─┴┘ bottom

    Args:
        box (str): Characters making up box.
        ascii (bool, optional): True if this box uses ascii characters only. Default is False.
    """

    def __init__(self, box: str, *, ascii: bool = False) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def substitute(
        self, options: ConsoleOptions, safe: bool = True
    ) -> "Box":
        ...

    def get_plain_headed_box(self) -> "Box":
        ...

    def get_top(self, widths: List[int]) -> str:
        ...

    def get_row(
        self,
        widths: List[int],
        level: Literal["head", "row", "mid", "foot"] = "row",
        edge: bool = True,
    ) -> str:
        ...

    def get_bottom(self, widths: List[int]) -> str:
        ...