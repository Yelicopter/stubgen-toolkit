from llama_index.core.embeddings import BaseEmbedding as BaseEmbedding
from private_gpt.settings.settings import Settings as Settings

class EmbeddingComponent:
    embedding_model: BaseEmbedding
    def __init__(self, settings: Settings) -> None: ...
