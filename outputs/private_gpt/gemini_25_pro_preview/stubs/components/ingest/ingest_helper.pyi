from pathlib import Path
from typing import Type

from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document

def _try_loading_included_file_formats() -> dict[str, Type[BaseReader]]: ...

FILE_READER_CLS: dict[str, Type[BaseReader]]

class IngestionHelper:
    @staticmethod
    def transform_file_into_documents(
        file_name: str, file_data: Path
    ) -> list[Document]: ...
    @staticmethod
    def _load_file_to_documents(file_name: str, file_data: Path) -> list[Document]: ...
    @staticmethod
    def _exclude_metadata(documents: list[Document]) -> None: ...