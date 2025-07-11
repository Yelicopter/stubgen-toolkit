from _typeshed import Incomplete
from llama_index.core.readers.base import BaseReader as BaseReader
from llama_index.core.schema import Document as Document
from pathlib import Path

logger: Incomplete
FILE_READER_CLS: Incomplete

class IngestionHelper:
    @staticmethod
    def transform_file_into_documents(file_name: str, file_data: Path) -> list[Document]: ...
