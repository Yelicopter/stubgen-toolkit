from __future__ import annotations

import platform
from typing import Any

from flake8.plugins.finder import Plugins


def information(version: str, plugins: Plugins) -> Any:
    ...