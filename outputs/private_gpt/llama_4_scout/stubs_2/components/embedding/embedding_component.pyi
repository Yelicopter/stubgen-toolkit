from injector import inject, singleton
from llama_index.core.embeddings import BaseEmbedding, MockEmbedding
from private_gpt.settings.settings import Settings

@singleton
class EmbeddingComponent:
    @inject
    def __init__(self, settings: Settings) -> None:
        ...

    def get_embedding_model(self) -> BaseEmbedding:
        ...