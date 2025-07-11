import os
import re
import typing
from typing import Any, Dict, TextIO

from yaml import SafeLoader

_env_replace_matcher: re.Pattern

def load_yaml_with_envvars(
    stream: TextIO, environ: Dict[str, str] = os.environ
) -> Dict[str, Any]: ...