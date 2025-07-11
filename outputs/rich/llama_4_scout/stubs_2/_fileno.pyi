from __future__ import annotations
from typing import IO, Any

def get_fileno(file_like: IO[Any]) -> int | None:
    """Get fileno() from a file, accounting for poorly implemented file-like objects.

    Args:
        file_like (IO): A file-like object.

    Returns:
        int | None: The result of fileno if available, or None if operation failed.
    """
    ...