from typing import Any, Optional
import pandas as pd

class VirtualDataFrame(pd.DataFrame):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...
    def head(self, n: int = 5) -> "VirtualDataFrame":
        ...