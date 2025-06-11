import configparser
from typing import IO, Dict, List, Mapping, Optional, Callable

from .default_styles import DEFAULT_STYLES
from .style import Style, StyleType

class Theme:
    styles: Dict[str, Style]
    def __init__(
        self, styles: Optional[Mapping[str, StyleType]] = None, inherit: bool = True
    ) -> None: ...
    @property
    def config(self) -> str: ...
    @classmethod
    def from_file(
        cls, config_file: IO[str], source: Optional[str] = None, inherit: bool = True
    ) -> "Theme": ...
    @classmethod
    def read(
        cls, path: str, inherit: bool = True, encoding: Optional[str] = None
    ) -> "Theme": ...

class ThemeStackError(Exception): ...

class ThemeStack:
    def __init__(self, theme: Theme) -> None: ...
    _entries: List[Dict[str, Style]]
    get: Callable[[str, Optional[Style]], Style]
    def push_theme(self, theme: Theme, inherit: bool = True) -> None: ...
    def pop_theme(self) -> None: ...