from __future__ import annotations

import argparse
from collections.abc import Sequence

NON_CODE_TOKENS: frozenset[int]

def check_docstring_first(src: bytes, filename: str = '<unknown>') -> int: ...

def main(argv: Sequence[str] | None = None) -> int: ...