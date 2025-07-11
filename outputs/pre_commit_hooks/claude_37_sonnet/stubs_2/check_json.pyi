from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from typing import Any, List, Optional, Tuple


def raise_duplicate_keys(
        ordered_pairs: List[Tuple[str, Any]],
) -> dict[str, Any]: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())