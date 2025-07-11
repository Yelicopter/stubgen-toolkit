from __future__ import annotations

import argparse
import re
from collections.abc import Sequence

FSTRING_START: int
FSTRING_END: int

START_QUOTE_RE: re.Pattern[str]

def handle_match(token_text: str) -> str: ...

def get_line_offsets_by_line_no(src: str) -> list[int]: ...

def fix_strings(filename: str) -> int: ...

def main(argv: Sequence[str] | None = None) -> int: ...