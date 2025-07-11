from llama_index.core.base.embeddings.base import BaseEmbedding
from pydantic import Field as Field, PrivateAttr as PrivateAttr

class SagemakerEmbedding(BaseEmbedding):
    endpoint_name: str
    @classmethod
    def class_name(cls) -> str: ...
