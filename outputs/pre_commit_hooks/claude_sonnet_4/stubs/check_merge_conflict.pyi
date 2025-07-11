from __future__ import annotations

import argparse
from collections.abc import Sequence

CONFLICT_PATTERNS: list[bytes]

def is_in_merge() -> bool: ...

def main(argv: Sequence[str] | None = None) -> int: ...