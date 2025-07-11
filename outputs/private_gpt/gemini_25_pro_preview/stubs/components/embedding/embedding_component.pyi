from llama_index.core.embeddings import BaseEmbedding

from private_gpt.settings.settings import Settings

class EmbeddingComponent:
    embedding_model: BaseEmbedding
    def __init__(self, settings: Settings) -> None: ...