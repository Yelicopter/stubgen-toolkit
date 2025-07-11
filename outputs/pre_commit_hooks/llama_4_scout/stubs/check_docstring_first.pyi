from __future__ import annotations

import argparse
import io
import tokenize
from collections.abc import Sequence
from tokenize import tokenize as tokenize_tokenize

NON_CODE_TOKENS: frozenset[int] = frozenset()

def check_docstring_first(src: bytes, filename: str = '<unknown>') -> int:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...