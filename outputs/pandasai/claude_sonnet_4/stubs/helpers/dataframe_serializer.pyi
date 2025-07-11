import json
import typing

if typing.TYPE_CHECKING:
    from ..dataframe.base import DataFrame

class DataframeSerializer:
    MAX_COLUMN_TEXT_LENGTH: int
    
    @classmethod
    def serialize(cls, df: DataFrame, dialect: str = "postgres") -> str: ...
    
    @classmethod
    def _truncate_dataframe(cls, df: DataFrame) -> DataFrame: ...