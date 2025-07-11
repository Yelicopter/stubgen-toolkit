from __future__ import annotations

import argparse
import io
import re
import sys
import tokenize
from collections.abc import Sequence
from typing import Dict, List, Optional

if sys.version_info >= (3, 12):  # pragma: >=3.12 cover
    FSTRING_START = tokenize.FSTRING_START
    FSTRING_END = tokenize.FSTRING_END
else:  # pragma: <3.12 cover
    FSTRING_START = FSTRING_END = -1

START_QUOTE_RE = re.compile('^[a-zA-Z]*"')


def handle_match(token_text: str) -> str: ...


def get_line_offsets_by_line_no(src: str) -> List[int]: ...


def fix_strings(filename: str) -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())