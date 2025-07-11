import logging
from collections.abc import Generator, Sequence
from flake8 import utils as utils

LOG: logging.Logger

def expand_paths(*, paths: Sequence[str], stdin_display_name: str, filename_patterns: Sequence[str], exclude: Sequence[str]) -> Generator[str, None, None]: ...
