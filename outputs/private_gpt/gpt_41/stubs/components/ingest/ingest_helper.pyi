import logging
from pathlib import Path

from llama_index.core.readers import StringIterableReader
from llama_index.core.readers.base import BaseReader
from llama_index.core.readers.json import JSONReader
from llama_index.core.schema import Document

def _try_loading_included_file_formats() -> dict[str, type]: ...
FILE_READER_CLS: dict[str, type]

class IngestionHelper:
    @staticmethod
    def transform_file_into_documents(
        file_name: str, file_data: Any
    ) -> list[Document]: ...
    @staticmethod
    def _load_file_to_documents(file_name: str, file_data: Any) -> list[Document]: ...
    @staticmethod
    def _exclude_metadata(documents: list[Document]) -> None: ...