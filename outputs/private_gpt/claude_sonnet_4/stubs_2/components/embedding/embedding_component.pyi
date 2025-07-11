import logging
from injector import inject, singleton
from llama_index.core.embeddings import BaseEmbedding, MockEmbedding
from private_gpt.paths import models_cache_path
from private_gpt.settings.settings import Settings

logger: logging.Logger

@singleton
class EmbeddingComponent:
    embedding_model: BaseEmbedding
    
    @inject
    def __init__(self, settings: Settings) -> None: ...