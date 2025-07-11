from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from typing import Any

def raise_duplicate_keys(ordered_pairs: Sequence[tuple[str, Any]]) -> dict[str, Any]:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...