from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Sequence
from re import Pattern

def _get_pattern(domain: str) -> Pattern[bytes]:
    ...

def _check_filename(filename: str, patterns: Sequence[Pattern[bytes]]) -> int:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...