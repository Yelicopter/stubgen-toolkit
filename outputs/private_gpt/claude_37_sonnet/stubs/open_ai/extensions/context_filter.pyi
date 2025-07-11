from pydantic import BaseModel, Field
from typing import List, Optional

class ContextFilter(BaseModel):
    docs_ids: Optional[List[str]] = Field(
        examples=[["c202d5e6-7b69-4869-81cc-dd574ee8ee11"]]
    )