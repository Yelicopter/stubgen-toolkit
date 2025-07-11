from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from re import Pattern
from typing import List, Optional


def _get_pattern(domain: str) -> Pattern[bytes]: ...


def _check_filename(filename: str, patterns: List[Pattern[bytes]]) -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())