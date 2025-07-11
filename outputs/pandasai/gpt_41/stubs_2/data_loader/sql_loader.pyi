from typing import Any
from .loader import DatasetLoader

class SQLDatasetLoader(DatasetLoader):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    def load(self) -> Any:
        ...