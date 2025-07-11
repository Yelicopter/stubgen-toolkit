from pydantic import BaseModel

class ContextFilter(BaseModel):
    docs_ids: list[str]
