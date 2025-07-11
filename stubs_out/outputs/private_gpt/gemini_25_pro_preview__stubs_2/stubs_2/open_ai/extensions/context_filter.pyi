from pydantic import BaseModel
from typing import Optional

class ContextFilter(BaseModel):
    docs_ids: Optional[list[str]]
