import configparser
import logging
import os.path
from typing import Any, Optional
from flake8.options.manager import OptionManager

LOG: logging.Logger

def _stat_key(s: str) -> tuple[int, int]: ...

def _find_config_file(path: str) -> Optional[str]: ...

def load_config(
    config: Optional[str],
    extra: list[str],
    *,
    isolated: bool = False,
) -> tuple[configparser.RawConfigParser, str]: ...

def parse_config(
    option_manager: OptionManager,
    cfg: configparser.RawConfigParser,
    cfg_dir: str,
) -> dict[str, Any]: ...