from typing import Any, Optional

LOG: Any
__version_info__: tuple[int, ...]
LOG_FORMAT: str

def configure_logging(verbosity: int, filename: Optional[str] = ..., logformat: str = ...) -> None: ...
