from pydantic import BaseModel, Field
from typing import Any, Literal

class CorsSettings(BaseModel):
    enabled: bool
    allow_credentials: bool
    allow_origins: list[str]
    allow_origin_regex: str | None
    allow_methods: list[str]
    allow_headers: list[str]

class AuthSettings(BaseModel):
    enabled: bool
    secret: str

class IngestionSettings(BaseModel):
    enabled: bool
    allow_ingest_from: list[str]

class ServerSettings(BaseModel):
    env_name: str
    port: int
    cors: CorsSettings
    auth: AuthSettings

class DataSettings(BaseModel):
    local_ingestion: IngestionSettings
    local_data_folder: str

class LLMSettings(BaseModel):
    max_new_tokens: int
    context_window: int
    temperature: float
    prompt_style: str

class VectorstoreSettings(BaseModel):
    database: Literal["chroma", "qdrant", "postgres", "clickhouse", "milvus"]

class NodeStoreSettings(BaseModel):
    database: Literal["simple", "postgres"]

class RagSettings(BaseModel):
    similarity_top_k: int
    similarity_value: float | None

class SummarizeSettings(BaseModel):
    use_async: bool

class Settings(BaseModel):
    server: ServerSettings
    data: DataSettings
    ui: Any
    llm: LLMSettings
    embedding: Any
    vectorstore: VectorstoreSettings
    nodestore: NodeStoreSettings
    rag: RagSettings
    summarize: SummarizeSettings