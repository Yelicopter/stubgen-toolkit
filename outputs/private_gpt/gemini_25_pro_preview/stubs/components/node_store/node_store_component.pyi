from llama_index.core.storage.docstore import BaseDocumentStore
from llama_index.core.storage.index_store.types import BaseIndexStore

from private_gpt.settings.settings import Settings

class NodeStoreComponent:
    index_store: BaseIndexStore
    doc_store: BaseDocumentStore
    def __init__(self, settings: Settings) -> None: ...