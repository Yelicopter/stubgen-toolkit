import json
from typing import Any

from pandasai.helpers.json_encoder import CustomJsonEncoder

class BaseResponse:
    def __init__(
        self,
        value: Any = None,
        type: str = None,
        last_code_executed: str = None,
        error: str = None,
    ) -> None:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def to_dict(self) -> Dict[str, Any]:
        ...

    def to_json(self) -> str:
        ...