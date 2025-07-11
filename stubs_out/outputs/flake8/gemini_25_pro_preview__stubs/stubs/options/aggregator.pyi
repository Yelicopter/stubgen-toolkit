import argparse
import configparser
import logging
from collections.abc import Sequence as Sequence
from flake8.options.manager import OptionManager as OptionManager

LOG: logging.Logger

def aggregate_options(manager: OptionManager, cfg: configparser.RawConfigParser, cfg_dir: str, argv: list[str] | None) -> argparse.Namespace: ...
