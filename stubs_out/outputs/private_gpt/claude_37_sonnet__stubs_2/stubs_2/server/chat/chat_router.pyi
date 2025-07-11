from fastapi import APIRouter as APIRouter, Depends as Depends, Request as Request
from llama_index.core.llms import ChatMessage as ChatMessage, MessageRole as MessageRole
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion as OpenAICompletion, OpenAIMessage as OpenAIMessage, to_openai_response as to_openai_response, to_openai_sse_stream as to_openai_sse_stream
from private_gpt.server.chat.chat_service import ChatService as ChatService
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel, ConfigDict, Field as Field
from starlette.responses import StreamingResponse as StreamingResponse
from typing import List, Optional, Union

chat_router: APIRouter

class ChatBody(BaseModel):
    messages: List[OpenAIMessage]
    use_context: bool
    context_filter: Optional[ContextFilter]
    include_sources: bool
    stream: bool
    model_config: ConfigDict

def chat_completion(request: Request, body: ChatBody) -> Union[OpenAICompletion, StreamingResponse]: ...
