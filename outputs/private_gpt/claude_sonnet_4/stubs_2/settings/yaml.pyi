import os
import re
import typing
from typing import Any, TextIO, Dict
from yaml import SafeLoader

_env_replace_matcher: re.Pattern[str]

@typing.no_type_check
def load_yaml_with_envvars(
    stream: TextIO, environ: Dict[str, str] = os.environ
) -> Dict[str, Any]: ...