from typing import Any, TextIO
from yaml import SafeLoader as SafeLoader

def load_yaml_with_envvars(stream: TextIO, environ: dict[str, str] = ...) -> Any: ...
