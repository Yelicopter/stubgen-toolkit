from __future__ import annotations

from collections.abc import Generator, Mapping, Sequence
from typing import TYPE_CHECKING, Any

from llama_index.core.schema import BaseNode
from llama_index.vector_stores.chroma import ChromaVectorStore

from private_gpt.utils.typing import T

if TYPE_CHECKING:
    from collections.abc import Mapping

def chunk_list(
    lst: Sequence[T], max_chunk_size: int
) -> Generator[Sequence[T], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: Any | None
    def __init__(
        self,
        chroma_client: Any,
        chroma_collection: Any,
        host: str | None = ...,
        port: str | None = ...,
        ssl: bool = ...,
        headers: Mapping[str, str] | None = ...,
        collection_kwargs: Mapping[str, Any] | None = ...,
    ) -> None: ...
    def add(self, nodes: list[BaseNode], **add_kwargs: Any) -> list[str]: ...