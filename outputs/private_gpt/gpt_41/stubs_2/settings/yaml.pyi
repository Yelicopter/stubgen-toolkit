import os
import re
import typing
from typing import Any, TextIO

from yaml import SafeLoader

def load_yaml_with_envvars(
    stream: TextIO, environ: dict[str, str] = ...
) -> Any: ...