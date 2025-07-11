from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import AbstractSet

def is_on_branch(
    protected: AbstractSet[str],
    patterns: AbstractSet[str] = frozenset(),
) -> bool: ...

def main(argv: Sequence[str] | None = None) -> int: ...