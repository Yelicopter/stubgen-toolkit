from __future__ import annotations

import logging
import os.path
from collections.abc import Generator, Sequence
from typing import Callable, Optional

from flake8 import utils

LOG = logging.getLogger(__name__)


def _filenames_from(
    arg: str,
    *,
    predicate: Callable[[str], bool],
) -> Generator[str, None, None]:
    ...


def expand_paths(
    *,
    paths: Sequence[str],
    stdin_display_name: str,
    filename_patterns: Sequence[str],
    exclude: Sequence[str],
) -> Generator[str, None, None]:
    ...