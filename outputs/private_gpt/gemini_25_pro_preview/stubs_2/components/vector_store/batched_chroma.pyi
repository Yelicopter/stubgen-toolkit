from __future__ import annotations

from collections.abc import Generator, Mapping, Sequence
from typing import TYPE_CHECKING, Any, TypeVar

import chromadb
from llama_index.core.schema import BaseNode
from llama_index.vector_stores.chroma import ChromaVectorStore

if TYPE_CHECKING:
    from collections.abc import Mapping

T = TypeVar("T")

def chunk_list(
    lst: Sequence[T], max_chunk_size: int
) -> Generator[Sequence[T], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: chromadb.Client | None
    def __init__(
        self,
        chroma_client: chromadb.Client,
        chroma_collection: chromadb.Collection,
        host: str | None = ...,
        port: str | None = ...,
        ssl: bool = ...,
        headers: Mapping[str, str] | None = ...,
        collection_kwargs: Mapping[str, Any] | None = ...,
    ) -> None: ...
    def add(self, nodes: list[BaseNode], **add_kwargs: Any) -> list[str]: ...