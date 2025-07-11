from collections.abc import Generator, Mapping, Sequence as Sequence
from llama_index.core.schema import BaseNode as BaseNode, MetadataMode as MetadataMode
from llama_index.core.vector_stores.utils import node_to_metadata_dict as node_to_metadata_dict
from llama_index.vector_stores.chroma import ChromaVectorStore
from typing import Any, List, Optional

def chunk_list(lst: List[BaseNode], max_chunk_size: int) -> Generator[List[BaseNode], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: Optional[Any]
    def __init__(self, chroma_client: Any, chroma_collection: Any, host: Optional[str] = ..., port: Optional[int] = ..., ssl: bool = ..., headers: Optional[Mapping[str, str]] = ..., collection_kwargs: Optional[Mapping[str, Any]] = ...) -> None: ...
    def add(self, nodes: List[BaseNode], **add_kwargs: Any) -> List[str]: ...
