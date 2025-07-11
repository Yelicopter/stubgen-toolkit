from llama_index.core.readers.base import BaseReader as BaseReader
from llama_index.core.schema import Document as Document
from pathlib import Path
from typing import Type

FILE_READER_CLS: dict[str, Type[BaseReader]]

class IngestionHelper:
    @staticmethod
    def transform_file_into_documents(file_name: str, file_data: Path) -> list[Document]: ...
