import chromadb
from collections.abc import Generator, Mapping, Sequence
from llama_index.core.schema import BaseNode as BaseNode
from llama_index.vector_stores.chroma import ChromaVectorStore
from typing import Any, TypeVar

T = TypeVar('T')

def chunk_list(lst: Sequence[T], max_chunk_size: int) -> Generator[Sequence[T], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: chromadb.Client | None
    def __init__(self, chroma_client: chromadb.Client, chroma_collection: chromadb.Collection, host: str | None = ..., port: str | None = ..., ssl: bool = ..., headers: Mapping[str, str] | None = ..., collection_kwargs: Mapping[str, Any] | None = ...) -> None: ...
    def add(self, nodes: list[BaseNode], **add_kwargs: Any) -> list[str]: ...
