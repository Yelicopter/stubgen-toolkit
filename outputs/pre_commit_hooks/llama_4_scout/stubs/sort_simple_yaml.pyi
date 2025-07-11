from __future__ import annotations

import argparse
from collections.abc import Sequence

QUOTES: list[str] = []

def sort(lines: Sequence[str]) -> list[str]:
    ...

def parse_block(lines: Sequence[str], header: bool = False) -> list[str]:
    ...

def parse_blocks(lines: Sequence[str]) -> list[list[str]]:
    ...

def first_key(lines: Sequence[str]) -> str:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...