from pydantic import BaseModel
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
    mode: Literal['llamacpp', 'openai', 'openailike', 'azopenai', 'sagemaker', 'mock', 'ollama', 'gemini']
    max_new_tokens: int
    context_window: int
    tokenizer: str | None
    temperature: float
    prompt_style: Literal['default', 'llama2', 'llama3', 'tag', 'mistral', 'chatml']

class VectorstoreSettings(BaseModel):
    database: Literal['chroma', 'qdrant', 'postgres', 'clickhouse', 'milvus']

class NodeStoreSettings(BaseModel):
    database: Literal['simple', 'postgres']

class LlamaCPPSettings(BaseModel):
    llm_hf_repo_id: str
    llm_hf_model_file: str
    tfs_z: float
    top_k: int
    top_p: float
    repeat_penalty: float

class HuggingFaceSettings(BaseModel):
    embedding_hf_model_name: str
    access_token: str | None
    trust_remote_code: bool

class EmbeddingSettings(BaseModel):
    mode: Literal['huggingface', 'openai', 'azopenai', 'sagemaker', 'ollama', 'mock', 'gemini', 'mistralai']
    ingest_mode: Literal['simple', 'batch', 'pipeline', 'parallel']
    count_workers: int
    embed_dim: int

class SagemakerSettings(BaseModel):
    llm_endpoint_name: str
    embedding_endpoint_name: str

class OpenAISettings(BaseModel):
    api_base: str | None
    api_key: str
    model: str
    request_timeout: float
    embedding_api_base: str | None
    embedding_api_key: str
    embedding_model: str

class GeminiSettings(BaseModel):
    api_key: str
    model: str
    embedding_model: str

class OllamaSettings(BaseModel):
    api_base: str
    embedding_api_base: str
    llm_model: str | None
    embedding_model: str | None
    keep_alive: str
    tfs_z: float
    num_predict: int | None
    top_k: int
    top_p: float
    repeat_last_n: int
    repeat_penalty: float
    request_timeout: float
    autopull_models: bool

class AzureOpenAISettings(BaseModel):
    api_key: str
    azure_endpoint: str
    api_version: str
    embedding_deployment_name: str
    embedding_model: str
    llm_deployment_name: str
    llm_model: str

class UISettings(BaseModel):
    enabled: bool
    path: str
    default_mode: Literal['RAG', 'Search', 'Basic', 'Summarize']
    default_chat_system_prompt: str | None
    default_query_system_prompt: str | None
    default_summarization_system_prompt: str | None
    delete_file_button_enabled: bool
    delete_all_files_button_enabled: bool

class RerankSettings(BaseModel):
    enabled: bool
    model: str
    top_n: int

class RagSettings(BaseModel):
    similarity_top_k: int
    similarity_value: float | None
    rerank: RerankSettings

class SummarizeSettings(BaseModel):
    use_async: bool

class ClickHouseSettings(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database: str
    secure: bool | None
    interface: str | None
    settings: dict[str, Any] | None
    connect_timeout: float | None
    send_receive_timeout: float | None
    verify: bool | str | None
    ca_cert: str | None
    client_cert: str | None
    client_cert_key: str | None
    http_proxy: str | None
    https_proxy: str | None
    server_host_name: str | None

class PostgresSettings(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str
    schema_name: str

class QdrantSettings(BaseModel):
    location: str | None
    url: str | None
    port: int | None
    grpc_port: int | None
    prefer_grpc: bool | None
    https: bool | None
    api_key: str | None
    prefix: str | None
    timeout: float | None
    host: str | None
    path: str | None
    force_disable_check_same_thread: bool

class MilvusSettings(BaseModel):
    uri: str
    token: str
    collection_name: str
    overwrite: bool

class Settings(BaseModel):
    server: ServerSettings
    data: DataSettings
    ui: UISettings
    llm: LLMSettings
    embedding: EmbeddingSettings
    llamacpp: LlamaCPPSettings
    huggingface: HuggingFaceSettings
    sagemaker: SagemakerSettings
    openai: OpenAISettings
    gemini: GeminiSettings
    ollama: OllamaSettings
    azopenai: AzureOpenAISettings
    vectorstore: VectorstoreSettings
    nodestore: NodeStoreSettings
    rag: RagSettings
    summarize: SummarizeSettings
    qdrant: QdrantSettings | None
    postgres: PostgresSettings | None
    clickhouse: ClickHouseSettings | None
    milvus: MilvusSettings | None

unsafe_settings: dict[str, Any]
unsafe_typed_settings: Settings

def settings() -> Settings: ...
