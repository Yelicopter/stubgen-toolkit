from typing import Optional

from pydantic import BaseModel, Field

class ContextFilter(BaseModel):
    docs_ids: Optional[list[str]] = Field(
        examples=[["c202d5e6-7b69-4869-81cc-dd574ee8ee11"]]
    )