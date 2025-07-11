from typing import Optional
import logging

LOG: logging.Logger
__version__: str
__version_info__: tuple[int, ...]
_VERBOSITY_TO_LOG_LEVEL: dict[int, int]
LOG_FORMAT: str

def configure_logging(
    verbosity: int,
    filename: Optional[str] = None,
    logformat: str = LOG_FORMAT,
) -> None: ...