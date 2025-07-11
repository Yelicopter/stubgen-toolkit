from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import IO

def fix_file(file_obj: IO[bytes]) -> int: ...

def main(argv: Sequence[str] | None = None) -> int: ...