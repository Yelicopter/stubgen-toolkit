import importlib
import types
from typing import Dict, Any, Optional

INSTALL_MAPPING: Dict[str, str]

def get_version(module: types.ModuleType) -> str: ...
def get_environment() -> Dict[str, Any]: ...
def import_dependency(
    name: str,
    extra: str = "",
    errors: str = "raise",
) -> Optional[types.ModuleType]: ...