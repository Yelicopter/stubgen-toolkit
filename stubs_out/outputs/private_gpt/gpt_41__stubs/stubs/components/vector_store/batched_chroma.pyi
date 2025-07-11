from collections.abc import Generator, Mapping as Mapping, Sequence as Sequence
from llama_index.core.schema import BaseNode as BaseNode, MetadataMode as MetadataMode
from llama_index.core.vector_stores.utils import node_to_metadata_dict as node_to_metadata_dict
from llama_index.vector_stores.chroma import ChromaVectorStore
from typing import Any

def chunk_list(lst: list[BaseNode], max_chunk_size: int) -> Generator[list[BaseNode], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: Any | None
    def __init__(self, chroma_client: Any, chroma_collection: Any, host: str | None = ..., port: int | None = ..., ssl: bool = ..., headers: dict | None = ..., collection_kwargs: dict | None = ...) -> None: ...
    def add(self, nodes: list[BaseNode], **add_kwargs: Any) -> list[str]: ...
