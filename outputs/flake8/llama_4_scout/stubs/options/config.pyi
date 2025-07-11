from __future__ import annotations

import configparser
import logging
import os.path
from typing import Any

from flake8 import exceptions
from flake8.defaults import VALID_CODE_PREFIX
from flake8.options.manager import OptionManager

LOG = logging.getLogger(__name__)


def _stat_key(s: str) -> Any:
    ...


def _find_config_file(path: str) -> Optional[str]:
    ...


def load_config(
    config: Optional[str],
    extra: Sequence[str],
    *,
    isolated: bool = False,
) -> tuple[configparser.RawConfigParser, str]:
    ...


def parse_config(
    option_manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
) -> dict:
    ...