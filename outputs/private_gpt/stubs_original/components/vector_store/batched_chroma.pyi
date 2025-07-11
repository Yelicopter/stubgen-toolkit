from collections.abc import Generator, Sequence
from llama_index.core.schema import BaseNode as BaseNode
from llama_index.vector_stores.chroma import ChromaVectorStore
from typing import Any

def chunk_list(lst: Sequence[BaseNode], max_chunk_size: int) -> Generator[Sequence[BaseNode], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: Any | None
    def __init__(self, chroma_client: Any, chroma_collection: Any, host: str | None = ..., port: str | None = ..., ssl: bool = ..., headers: dict[str, str] | None = ..., collection_kwargs: dict[Any, Any] | None = ...) -> None: ...
    def add(self, nodes: Sequence[BaseNode], **add_kwargs: Any) -> list[str]: ...
