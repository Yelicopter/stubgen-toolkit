from pydantic import BaseModel, Field

class ContextFilter(BaseModel):
    docs_ids: list[str] | None