import argparse
import logging
from flake8.formatting.base import BaseFormatter as BaseFormatter
from flake8.plugins.finder import LoadedPlugin as LoadedPlugin

LOG: logging.Logger

def make(reporters: dict[str, LoadedPlugin], options: argparse.Namespace) -> BaseFormatter: ...
