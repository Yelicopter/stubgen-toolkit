from __future__ import annotations

import sys
from collections.abc import Sequence

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

def main(argv: Sequence[str] | None = None) -> int: ...