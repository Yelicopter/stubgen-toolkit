from __future__ import annotations

import logging
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Sequence

LOG: logging.Logger

def _filenames_from(arg: str, *, predicate: Callable[[str], bool]) -> Generator[str, None, None]: ...
def expand_paths(
    *,
    paths: Sequence[str],
    stdin_display_name: str,
    filename_patterns: Sequence[str],
    exclude: Sequence[str],
) -> Generator[str, None, None]: ...