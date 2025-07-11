from llama_index.core.llms import CustomLLM, LLMMetadata
from typing import Any, Sequence

class SagemakerLLM(CustomLLM):
    endpoint_name: str
    temperature: float
    max_new_tokens: int
    context_window: int

    _boto_client: Any

    def __init__(
        self,
        endpoint_name: str,
        temperature: float,
        max_new_tokens: int,
        context_window: int,
    ) -> None:
        ...

    @property
    def inference_params(self) -> dict[str, Any]:
        ...

    @property
    def metadata(self) -> LLMMetadata:
        ...

    def complete(self, prompt: str, **kwargs: Any) -> Any:
        ...

    def stream_complete(self, prompt: str, **kwargs: Any) -> Any:
        ...

    def chat(self, messages: Sequence[Any], **kwargs: Any) -> Any:
        ...

    def stream_chat(self, messages: Sequence[Any], **kwargs: Any) -> Any:
        ...