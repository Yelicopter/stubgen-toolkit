from typing import Optional

LOG: ...
__version_info__: tuple[int, ...]
LOG_FORMAT: str

def configure_logging(verbosity: int, filename: Optional[str] = ..., logformat: str = ...) -> None: ...
