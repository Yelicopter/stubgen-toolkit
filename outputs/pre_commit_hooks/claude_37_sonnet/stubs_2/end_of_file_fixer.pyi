from __future__ import annotations

import argparse
import os
from collections.abc import Sequence
from typing import IO, Optional


def fix_file(file_obj: IO[bytes]) -> int: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())