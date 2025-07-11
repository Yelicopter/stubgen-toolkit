import configparser
import logging
from flake8.options.manager import OptionManager as OptionManager
from typing import Any

LOG: logging.Logger

def load_config(config: str | None, extra: list[str], *, isolated: bool = ...) -> tuple[configparser.RawConfigParser, str]: ...
def parse_config(option_manager: OptionManager, cfg: configparser.RawConfigParser, cfg_dir: str) -> dict[str, Any]: ...
