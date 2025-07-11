from __future__ import annotations

import argparse
import collections
from collections.abc import Sequence
from typing import DefaultDict, Dict, Literal, Optional, Union


CRLF = b'\r\n'
LF = b'\n'
CR = b'\r'
# Prefer LF to CRLF to CR, but detect CRLF before LF
ALL_ENDINGS = (CR, CRLF, LF)
FIX_TO_LINE_ENDING = {'cr': CR, 'crlf': CRLF, 'lf': LF}


def _fix(filename: str, contents: bytes, ending: bytes) -> None: ...


def fix_filename(filename: str, fix: str) -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())