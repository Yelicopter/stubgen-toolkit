import logging
from llama_index.core.readers import StringIterableReader as StringIterableReader
from llama_index.core.readers.base import BaseReader as BaseReader
from llama_index.core.readers.json import JSONReader as JSONReader
from llama_index.core.schema import Document as Document
from pathlib import Path
from typing import Dict, List, Type

logger: logging.Logger
FILE_READER_CLS: Dict[str, Type[BaseReader]]

class IngestionHelper:
    @staticmethod
    def transform_file_into_documents(file_name: str, file_data: Path) -> List[Document]: ...
