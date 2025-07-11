import logging
from llama_index.core.embeddings import BaseEmbedding as BaseEmbedding, MockEmbedding as MockEmbedding
from private_gpt.settings.settings import Settings as Settings

logger: logging.Logger

class EmbeddingComponent:
    embedding_model: BaseEmbedding
    def __init__(self, settings: Settings) -> None: ...
