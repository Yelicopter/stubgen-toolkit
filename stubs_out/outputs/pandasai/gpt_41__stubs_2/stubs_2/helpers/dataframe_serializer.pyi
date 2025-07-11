from typing import Any

class DataframeSerializer:
    MAX_COLUMN_TEXT_LENGTH: int
    @classmethod
    def serialize(cls, df: Any, dialect: str = ...) -> str: ...
