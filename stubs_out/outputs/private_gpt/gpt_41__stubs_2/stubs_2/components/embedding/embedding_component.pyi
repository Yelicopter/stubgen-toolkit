from llama_index.core.embeddings import BaseEmbedding as BaseEmbedding, MockEmbedding as MockEmbedding
from private_gpt.paths import models_cache_path as models_cache_path
from private_gpt.settings.settings import Settings as Settings

class EmbeddingComponent:
    embedding_model: BaseEmbedding
    def __init__(self, settings: Settings) -> None: ...
