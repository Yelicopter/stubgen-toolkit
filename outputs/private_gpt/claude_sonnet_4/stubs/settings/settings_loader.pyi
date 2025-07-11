import functools
import logging
import os
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any, List, Dict

from pydantic.v1.utils import deep_update, unique_list
from private_gpt.constants import PROJECT_ROOT_PATH
from private_gpt.settings.yaml import load_yaml_with_envvars

logger: logging.Logger

_settings_folder: str
_test_profile: List[str]
active_profiles: List[str]

def merge_settings(settings: Iterable[Dict[str, Any]]) -> Dict[str, Any]: ...
def load_settings_from_profile(profile: str) -> Dict[str, Any]: ...
def load_active_settings() -> Dict[str, Any]: ...