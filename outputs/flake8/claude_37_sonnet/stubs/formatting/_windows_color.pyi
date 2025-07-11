from __future__ import annotations

import sys

terminal_supports_color: bool

if sys.platform == "win32":
    def _enable() -> None: ...