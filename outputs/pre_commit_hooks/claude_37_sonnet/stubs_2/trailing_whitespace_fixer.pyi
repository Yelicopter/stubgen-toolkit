from __future__ import annotations

import argparse
import os
from collections.abc import Sequence
from typing import List, Optional


def _fix_file(
        filename: str,
        is_markdown: bool,
        chars: Optional[bytes],
) -> bool: ...


def _process_line(
        line: bytes,
        is_markdown: bool,
        chars: Optional[bytes],
) -> bytes: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())