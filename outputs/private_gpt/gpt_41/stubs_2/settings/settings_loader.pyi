import functools
import logging
import os
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from pydantic.v1.utils import deep_update, unique_list

from private_gpt.constants import PROJECT_ROOT_PATH
from private_gpt.settings.yaml import load_yaml_with_envvars

active_profiles: list[str]

def merge_settings(settings: list[dict[str, Any]]) -> dict[str, Any]: ...
def load_settings_from_profile(profile: str) -> dict[str, Any]: ...
def load_active_settings() -> dict[str, Any]: ...