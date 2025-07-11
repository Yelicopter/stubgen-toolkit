from typing import Dict, List, Optional, Union

from .default_styles import DEFAULT_STYLES
from .style import Style, StyleType
from .terminal_theme import TerminalTheme

class Theme:
    def __init__(
        self,
        styles: Optional[Dict[str, StyleType]] = None,
        inherit: bool = True,
    ) -> None: ...
    
    @property
    def styles(self) -> Dict[str, Style]: ...
    
    def read(self, name: str, default: Optional[StyleType] = None) -> Optional[Style]: ...

class ThemeStack:
    def __init__(self, theme: Theme) -> None: ...
    
    @property
    def top(self) -> Theme: ...
    
    def get(self, name: str) -> Optional[Style]: ...
    def push_theme(self, theme: Theme, inherit: bool = True) -> None: ...
    def pop_theme(self) -> Theme: ...