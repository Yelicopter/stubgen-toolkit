from collections.abc import Iterator
from llama_index.core.llms import ChatResponse as ChatResponse, CompletionResponse as CompletionResponse
from private_gpt.server.chunks.chunks_service import Chunk as Chunk
from pydantic import BaseModel
from typing import List, Literal, Optional, Union

class OpenAIDelta(BaseModel):
    content: Optional[str]

class OpenAIMessage(BaseModel):
    role: Literal['user', 'assistant', 'system']
    content: Optional[str]

class OpenAIChoice(BaseModel):
    finish_reason: Optional[str]
    delta: Optional[OpenAIDelta]
    message: Optional[OpenAIMessage]
    sources: Optional[List[Chunk]]
    index: int

class OpenAICompletion(BaseModel):
    id: str
    object: Literal['completion', 'completion.chunk']
    created: int
    model: Literal['private-gpt']
    choices: List[OpenAIChoice]
    @classmethod
    def from_text(cls, text: Optional[str], finish_reason: Optional[str] = ..., sources: Optional[List[Chunk]] = ...) -> OpenAICompletion: ...
    @classmethod
    def json_from_delta(cls, *, text: Optional[str], finish_reason: Optional[str] = ..., sources: Optional[List[Chunk]] = ...) -> str: ...

def to_openai_response(response: Union[str, ChatResponse], sources: Optional[List[Chunk]] = ...) -> OpenAICompletion: ...
def to_openai_sse_stream(response_generator: Iterator[Union[str, CompletionResponse, ChatResponse]], sources: Optional[List[Chunk]] = ...) -> Iterator[str]: ...
