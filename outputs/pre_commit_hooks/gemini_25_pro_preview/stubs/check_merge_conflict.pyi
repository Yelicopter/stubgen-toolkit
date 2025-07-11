from __future__ import annotations

from collections.abc import Sequence
from typing import Final

CONFLICT_PATTERNS: Final[list[bytes]]

def is_in_merge() -> bool: ...
def main(argv: Sequence[str] | None = None) -> int: ...