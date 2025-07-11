from __future__ import annotations

import logging
import sys
from typing import Optional

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.NullHandler())

__version__ = "7.3.0"
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())

_VERBOSITY_TO_LOG_LEVEL = {
    1: logging.INFO,  
    2: logging.DEBUG,  
}

LOG_FORMAT = (
    "%(name)-25s %(processName)-11s %(relativeCreated)6d "
    "%(levelname)-8s %(message)s"
)


def configure_logging(
    verbosity: int, 
    filename: Optional[str] = None, 
    logformat: str = LOG_FORMAT,
) -> None:
    ...