from typing import Any
from .sql_loader import SQLDatasetLoader

class ViewDatasetLoader(SQLDatasetLoader):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    def load(self) -> Any:
        ...