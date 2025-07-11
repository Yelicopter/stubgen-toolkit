from typing import Any, Dict

from pandasai.config import Config
from pandasai.core.code_execution.environment import get_environment
from pandasai.exceptions import CodeExecutionError, NoResultFoundError

class CodeExecutor:
    def __init__(self, config: Config) -> None:
        ...

    def add_to_env(self, key: str, value: Any) -> None:
        ...

    def execute(self, code: str) -> Dict[str, Any]:
        ...

    def execute_and_return_result(self, code: str) -> Any:
        ...

    @property
    def environment(self) -> Dict[str, Any]:
        ...