from llama_index.core.readers import StringIterableReader as StringIterableReader
from llama_index.core.readers.base import BaseReader as BaseReader
from llama_index.core.readers.json import JSONReader as JSONReader
from llama_index.core.schema import Document as Document
from pathlib import Path as Path
from typing import Any

FILE_READER_CLS: dict[str, type]

class IngestionHelper:
    @staticmethod
    def transform_file_into_documents(file_name: str, file_data: Any) -> list[Document]: ...
