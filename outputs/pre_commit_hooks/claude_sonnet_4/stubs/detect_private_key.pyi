from __future__ import annotations

import argparse
from collections.abc import Sequence

BLACKLIST: list[bytes]

def main(argv: Sequence[str] | None = None) -> int: ...