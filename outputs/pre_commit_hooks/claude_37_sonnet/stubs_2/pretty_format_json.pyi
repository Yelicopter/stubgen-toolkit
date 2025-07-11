from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping, Sequence
from difflib import unified_diff
from typing import Any, Dict, List, Optional, Tuple, Union


def _get_pretty_format(
        contents: str,
        indent: Union[int, str],
        ensure_ascii: bool = True,
        sort_keys: bool = True,
        top_keys: Tuple[str, ...] = (),
) -> str: ...


def _autofix(filename: str, new_contents: str) -> None: ...


def parse_num_to_int(s: str) -> Union[int, str]: ...


def parse_topkeys(s: str) -> List[str]: ...


def get_diff(source: str, target: str, file: str) -> str: ...


def main(argv: Optional[Sequence[str]] = None) -> int: ...


if __name__ == '__main__':
    raise SystemExit(main())