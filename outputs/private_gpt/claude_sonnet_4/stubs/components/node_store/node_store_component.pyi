import logging
from injector import inject, singleton
from llama_index.core.storage.docstore import BaseDocumentStore, SimpleDocumentStore
from llama_index.core.storage.index_store import SimpleIndexStore
from llama_index.core.storage.index_store.types import BaseIndexStore
from private_gpt.paths import local_data_path
from private_gpt.settings.settings import Settings

logger: logging.Logger

@singleton
class NodeStoreComponent:
    index_store: BaseIndexStore
    doc_store: BaseDocumentStore
    
    @inject
    def __init__(self, settings: Settings) -> None: ...