from collections.abc import Generator, Sequence
from typing import TYPE_CHECKING, Any, List, Optional
from llama_index.core.schema import BaseNode, MetadataMode
from llama_index.core.vector_stores.utils import node_to_metadata_dict
from llama_index.vector_stores.chroma import ChromaVectorStore

if TYPE_CHECKING:
    from collections.abc import Mapping

def chunk_list(
    lst: List[BaseNode], max_chunk_size: int
) -> Generator[List[BaseNode], None, None]: ...

class BatchedChromaVectorStore(ChromaVectorStore):
    chroma_client: Optional[Any]
    
    def __init__(
        self,
        chroma_client: Any,
        chroma_collection: Any,
        host: Optional[str] = None,
        port: Optional[int] = None,
        ssl: bool = False,
        headers: Optional[Mapping[str, str]] = None,
        collection_kwargs: Optional[Mapping[str, Any]] = None,
    ) -> None: ...
    
    def add(self, nodes: List[BaseNode], **add_kwargs: Any) -> List[str]: ...