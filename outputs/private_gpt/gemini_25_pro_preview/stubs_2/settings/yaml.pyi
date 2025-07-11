import os
import re
from typing import Any, TextIO

_env_replace_matcher: re.Pattern[str]

def load_yaml_with_envvars(
    stream: TextIO, environ: dict[str, str] = ...
) -> Any: ...