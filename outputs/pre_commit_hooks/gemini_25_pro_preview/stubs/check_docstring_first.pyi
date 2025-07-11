from __future__ import annotations

from collections.abc import Sequence
from typing import Final

NON_CODE_TOKENS: Final[frozenset[int]]

def check_docstring_first(src: bytes, filename: str = ...) -> int: ...
def main(argv: Sequence[str] | None = None) -> int: ...