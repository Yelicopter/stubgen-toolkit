from __future__ import annotations

import argparse
from collections.abc import Mapping
from collections.abc import Sequence

def _get_pretty_format(
    contents: str,
    indent: str | int,
    ensure_ascii: bool = True,
    sort_keys: bool = True,
    top_keys: Sequence[str] = (),
) -> str: ...

def _autofix(filename: str, new_contents: str) -> None: ...

def parse_num_to_int(s: str) -> int | str: ...

def parse_topkeys(s: str) -> list[str]: ...

def get_diff(source: str, target: str, file: str) -> str: ...

def main(argv: Sequence[str] | None = None) -> int: ...