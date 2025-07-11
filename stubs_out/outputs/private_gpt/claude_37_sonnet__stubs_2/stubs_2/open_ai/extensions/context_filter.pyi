from pydantic import BaseModel
from typing import List, Optional

class ContextFilter(BaseModel):
    docs_ids: Optional[List[str]]
