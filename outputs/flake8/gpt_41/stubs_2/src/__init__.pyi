from typing import Any, Optional

LOG: Any
__version__: str
__version_info__: tuple[int, ...]
_VERBOSITY_TO_LOG_LEVEL: dict[int, int]
LOG_FORMAT: str

def configure_logging(
    verbosity: int,
    filename: Optional[str] = ...,
    logformat: str = ...,
) -> None: ...