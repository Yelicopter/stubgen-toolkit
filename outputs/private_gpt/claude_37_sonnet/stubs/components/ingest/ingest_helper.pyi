import logging
from pathlib import Path
from typing import Dict, List, Type

from llama_index.core.readers import StringIterableReader
from llama_index.core.readers.base import BaseReader
from llama_index.core.readers.json import JSONReader
from llama_index.core.schema import Document

logger: logging.Logger

def _try_loading_included_file_formats() -> Dict[str, Type[BaseReader]]: ...

FILE_READER_CLS: Dict[str, Type[BaseReader]]

class IngestionHelper:
    @staticmethod
    def transform_file_into_documents(
        file_name: str, file_data: Path
    ) -> List[Document]: ...
    
    @staticmethod
    def _load_file_to_documents(file_name: str, file_data: Path) -> List[Document]: ...
    
    @staticmethod
    def _exclude_metadata(documents: List[Document]) -> None: ...