from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from typing import Optional

if sys.version_info >= (3, 11):  # pragma: >=3.11 cover
    import tomllib
else:  # pragma: <3.11 cover
    import tomli as tomllib


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())