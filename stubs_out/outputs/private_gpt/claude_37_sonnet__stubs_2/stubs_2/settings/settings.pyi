from private_gpt.settings.settings_loader import load_active_settings as load_active_settings
from pydantic import BaseModel
from typing import Any, Dict, List, Literal, Optional

class CorsSettings(BaseModel):
    enabled: bool
    allow_credentials: bool
    allow_origins: List[str]
    allow_origin_regex: Optional[str]
    allow_methods: List[str]
    allow_headers: List[str]

class AuthSettings(BaseModel):
    enabled: bool
    secret: str

class IngestionSettings(BaseModel):
    enabled: bool
    allow_ingest_from: List[str]

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
    tokenizer: Optional[str]
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
    access_token: Optional[str]
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
    api_base: Optional[str]
    api_key: str
    model: str
    request_timeout: float
    embedding_api_base: Optional[str]
    embedding_api_key: Optional[str]
    embedding_model: str

class GeminiSettings(BaseModel):
    api_key: str
    model: str
    embedding_model: str

class OllamaSettings(BaseModel):
    api_base: str
    embedding_api_base: str
    llm_model: Optional[str]
    embedding_model: Optional[str]
    keep_alive: str
    tfs_z: float
    num_predict: Optional[int]
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
    default_chat_system_prompt: Optional[str]
    default_query_system_prompt: Optional[str]
    default_summarization_system_prompt: Optional[str]
    delete_file_button_enabled: bool
    delete_all_files_button_enabled: bool

class RerankSettings(BaseModel):
    enabled: bool
    model: str
    top_n: int

class RagSettings(BaseModel):
    similarity_top_k: int
    similarity_value: Optional[float]
    rerank: RerankSettings

class SummarizeSettings(BaseModel):
    use_async: bool

class ClickHouseSettings(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database: str
    secure: Optional[bool]
    interface: Optional[str]
    settings: Optional[Dict[str, Any]]
    connect_timeout: Optional[int]
    send_receive_timeout: Optional[int]
    verify: Optional[bool]
    ca_cert: Optional[str]
    client_cert: Optional[str]
    client_cert_key: Optional[str]
    http_proxy: Optional[str]
    https_proxy: Optional[str]
    server_host_name: Optional[str]

class PostgresSettings(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str
    schema_name: str

class QdrantSettings(BaseModel):
    location: Optional[str]
    url: Optional[str]
    port: Optional[int]
    grpc_port: Optional[int]
    prefer_grpc: Optional[bool]
    https: Optional[bool]
    api_key: Optional[str]
    prefix: Optional[str]
    timeout: Optional[float]
    host: Optional[str]
    path: Optional[str]
    force_disable_check_same_thread: Optional[bool]

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
    qdrant: Optional[QdrantSettings]
    postgres: Optional[PostgresSettings]
    clickhouse: Optional[ClickHouseSettings]
    milvus: Optional[MilvusSettings]

unsafe_settings: Dict[str, Any]
unsafe_typed_settings: Settings

def settings() -> Settings: ...
