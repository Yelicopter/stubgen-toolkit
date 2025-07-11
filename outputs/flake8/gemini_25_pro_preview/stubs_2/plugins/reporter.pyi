from __future__ import annotations

import argparse
import logging

from flake8.formatting.base import BaseFormatter
from flake8.plugins.finder import LoadedPlugin

LOG: logging.Logger

def make(reporters: dict[str, LoadedPlugin], options: argparse.Namespace) -> BaseFormatter: ...