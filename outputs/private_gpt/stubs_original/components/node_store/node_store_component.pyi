from _typeshed import Incomplete
from llama_index.core.storage.docstore import BaseDocumentStore as BaseDocumentStore
from llama_index.core.storage.index_store.types import BaseIndexStore as BaseIndexStore
from private_gpt.paths import local_data_path as local_data_path
from private_gpt.settings.settings import Settings as Settings

logger: Incomplete

class NodeStoreComponent:
    index_store: BaseIndexStore
    doc_store: BaseDocumentStore
    def __init__(self, settings: Settings) -> None: ...
