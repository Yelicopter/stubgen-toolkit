from typing import Any

class ColorBox:
    def __rich_console__(self, console: Any, options: Any) -> Any:
        ...
    
    def __rich_measure__(self, console: Any, options: Any) -> Any:
        ...

def make_test_card() -> Any:
    ...