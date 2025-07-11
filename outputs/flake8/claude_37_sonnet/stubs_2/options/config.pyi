from __future__ import annotations

import configparser
import logging
import os.path
from typing import Any, Dict, Optional, Tuple, Union

from flake8 import exceptions
from flake8.defaults import VALID_CODE_PREFIX
from flake8.options.manager import OptionManager

LOG: logging.Logger

def _stat_key(s: str) -> Tuple[int, int]: ...

def _find_config_file(path: str) -> Optional[str]: ...

def load_config(
    config: Optional[str],
    extra: list[str],
    *,
    isolated: bool = False,
) -> Tuple[configparser.RawConfigParser, str]: ...

def parse_config(
    option_manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
) -> Dict[str, Any]: ...