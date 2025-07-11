from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import IO

PASS: int
FAIL: int

class Requirement:
    UNTIL_COMPARISON: re.Pattern[bytes]
    UNTIL_SEP: re.Pattern[bytes]
    value: bytes | None
    comments: list[bytes]
    
    def __init__(self) -> None: ...
    
    @property
    def name(self) -> bytes: ...
    
    def __lt__(self, requirement: Requirement) -> bool: ...
    def is_complete(self) -> bool: ...
    def append_value(self, value: bytes) -> None: ...

def fix_requirements(f: IO[bytes]) -> int: ...

def main(argv: Sequence[str] | None = None) -> int: ...