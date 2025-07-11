from __future__ import annotations

import argparse
import io
import tokenize
from collections.abc import Sequence
from tokenize import tokenize as tokenize_tokenize
from typing import Optional

NON_CODE_TOKENS = frozenset((
    tokenize.COMMENT, tokenize.ENDMARKER, tokenize.NEWLINE, tokenize.NL,
    tokenize.ENCODING,
))


def check_docstring_first(src: bytes, filename: str = '<unknown>') -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...