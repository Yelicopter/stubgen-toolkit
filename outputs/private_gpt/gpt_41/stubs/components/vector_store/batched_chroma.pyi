from collections.abc import Generator, Sequence
from typing import TYPE_CHECKING, Any

from llama_index.core.schema import BaseNode, MetadataMode
from llama_index.core.vector_stores.utils import node_to_metadata_dict
from llama_index.vector_stores.chroma import ChromaVectorStore

if TYPE_CHECKING:
    from collections.abc import Mapping

def chunk_list(
    lst: list[BaseNode], max_chunk_size: int
) -> Generator[list[BaseNode], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: Any | None
    def __init__(
        self,
        chroma_client: Any,
        chroma_collection: Any,
        host: str | None = None,
        port: int | None = None,
        ssl: bool = False,
        headers: dict | None = None,
        collection_kwargs: dict | None = None,
    ) -> None: ...
    def add(self, nodes: list[BaseNode], **add_kwargs: Any) -> list[str]: ...