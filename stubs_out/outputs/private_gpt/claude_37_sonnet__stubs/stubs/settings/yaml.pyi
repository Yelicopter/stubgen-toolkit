from typing import Any, Dict, TextIO
from yaml import SafeLoader as SafeLoader

def load_yaml_with_envvars(stream: TextIO, environ: Dict[str, str] = ...) -> Dict[str, Any]: ...
