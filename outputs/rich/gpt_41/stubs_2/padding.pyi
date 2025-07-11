from typing import Any, List, Optional, Tuple, Union

PaddingDimensions = Union[int, Tuple[int], Tuple[int, int], Tuple[int, int, int, int]]

class Padding:
    def __init__(
        self,
        renderable: Any,
        pad: PaddingDimensions = ...,
        *,
        style: str = ...,
        expand: bool = ...,
    ) -> None: ...
    @classmethod
    def indent(cls, renderable: Any, level: int) -> "Padding": ...
    @staticmethod
    def unpack(pad: PaddingDimensions) -> Tuple[int, int, int, int]: ...
    def __repr__(self) -> str: ...
    def __rich_console__(self, console: Any, options: Any) -> Any: ...
    def __rich_measure__(self, console: Any, options: Any) -> Any: ...