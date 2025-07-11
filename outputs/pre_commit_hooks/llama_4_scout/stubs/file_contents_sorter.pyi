from __future__ import annotations

import argparse
from collections.abc import Iterable
from collections.abc import Sequence
from typing import Any
from typing import Callable
from typing import IO

PASS: int = 0
FAIL: int = 1

def sort_file_contents(
    f: IO[bytes],
    key: Callable[[bytes], Any],
    *,
    unique: bool = False,
) -> int:
    ...

def main(argv: Sequence[str] | None = None) -> int:
    ...