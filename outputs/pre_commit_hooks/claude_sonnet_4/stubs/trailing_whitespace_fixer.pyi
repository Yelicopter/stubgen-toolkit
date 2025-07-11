from __future__ import annotations

import argparse
from collections.abc import Sequence

def _fix_file(
    filename: str,
    is_markdown: bool,
    chars: bytes | None,
) -> bool: ...

def _process_line(
    line: bytes,
    is_markdown: bool,
    chars: bytes | None,
) -> bytes: ...

def main(argv: Sequence[str] | None = None) -> int: ...