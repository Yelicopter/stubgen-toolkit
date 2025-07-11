from typing import Any, Dict, Iterable, Optional, Tuple, Union
from .console import Console, ConsoleOptions, RenderResult

def _get_signature(obj: Any) -> Optional[str]: ...

class Inspect:
    def __init__(
        self,
        obj: Any,
        *,
        title: Optional[str] = None,
        help: bool = False,
        methods: bool = False,
        docs: bool = True,
        private: bool = False,
        dunder: bool = False,
        sort: bool = True,
        all: bool = False,
        value: bool = True
    ) -> None: ...
    
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...

def inspect(
    obj: Any,
    *,
    console: Optional[Console] = None,
    title: Optional[str] = None,
    help: bool = False,
    methods: bool = False,
    docs: bool = True,
    private: bool = False,
    dunder: bool = False,
    sort: bool = True,
    all: bool = False,
    value: bool = True
) -> None: ...