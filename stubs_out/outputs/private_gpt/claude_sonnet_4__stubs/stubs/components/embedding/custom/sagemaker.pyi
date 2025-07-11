from llama_index.core.base.embeddings.base import BaseEmbedding

class SagemakerEmbedding(BaseEmbedding):
    endpoint_name: str
    @classmethod
    def class_name(cls) -> str: ...
