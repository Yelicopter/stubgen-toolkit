from __future__ import annotations

import argparse
import collections
from collections.abc import Sequence

CRLF: bytes = b''
LF: bytes = b''
CR: bytes = b''

ALL_ENDINGS: tuple[bytes, ...] = ()
FIX_TO_LINE_ENDING: dict[str, bytes] = {}

def _fix(filename: str, contents: bytes, ending: bytes) -> None:
    ...

def fix_filename(filename: str, fix: str) -> bool:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...