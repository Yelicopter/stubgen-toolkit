from __future__ import annotations

import argparse
import logging

from flake8.formatting.base import BaseFormatter
from flake8.plugins.finder import LoadedPlugin

LOG = logging.getLogger(__name__)


def make(
    reporters: dict[str, LoadedPlugin],
    options: Any,
) -> BaseFormatter:
    ...