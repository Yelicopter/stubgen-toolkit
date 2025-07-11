from ..dataframe.base import DataFrame as DataFrame

class DataframeSerializer:
    MAX_COLUMN_TEXT_LENGTH: int
    @classmethod
    def serialize(cls, df: DataFrame, dialect: str = ...) -> str: ...
