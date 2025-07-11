from injector import inject, singleton
from llama_index.core.storage.docstore import BaseDocumentStore
from llama_index.core.storage.index_store import BaseIndexStore
from private_gpt.settings.settings import Settings

@singleton
class NodeStoreComponent:
    @inject
    def __init__(self, settings: Settings) -> None:
        ...

    def get_index_store(self) -> BaseIndexStore:
        ...

    def get_doc_store(self) -> BaseDocumentStore:
        ...