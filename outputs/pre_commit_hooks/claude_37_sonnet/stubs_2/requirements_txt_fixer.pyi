from __future__ import annotations

import argparse
import re
from collections.abc import Sequence
from typing import IO, List, Optional


PASS = 0
FAIL = 1


class Requirement:
    UNTIL_COMPARISON = re.compile(b'={2,3}|!=|~=|>=?|<=?')
    UNTIL_SEP = re.compile(rb'[^;\s]+')

    def __init__(self) -> None:
        self.value: Optional[bytes] = None
        self.comments: List[bytes] = []

    @property
    def name(self) -> bytes: ...

    def __lt__(self, requirement: 'Requirement') -> bool: ...

    def is_complete(self) -> bool: ...

    def append_value(self, value: bytes) -> None: ...


def fix_requirements(f: IO[bytes]) -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())