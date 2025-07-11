from __future__ import annotations

import argparse
import io
import re
import sys
import tokenize
from collections.abc import Sequence

if sys.version_info >= (3, 12):
    FSTRING_START = tokenize.FSTRING_START
    FSTRING_END = tokenize.FSTRING_END
else:
    FSTRING_START = FSTRING_END = -1

START_QUOTE_RE: re.Pattern[str] = ...

def handle_match(token_text: str) -> str:
    ...

def get_line_offsets_by_line_no(src: str) -> list[int]:
    ...

def fix_strings(filename: str) -> int:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...