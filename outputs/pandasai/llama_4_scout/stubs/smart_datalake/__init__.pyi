import uuid
import warnings
from typing import List, Optional, Union

import pandas as pd

from pandasai.agent import Agent
from pandasai.dataframe.base import DataFrame

from ..config import Config


class SmartDatalake:
    def __init__(
        self,
        dfs: List[pd.DataFrame],
        config: Config | None = None,
    ) -> None:
        ...

    def load_dfs(self, dfs: List[pd.DataFrame]) -> List[DataFrame]:
        ...

    def chat(self, query: str, output_type: str | None = None) -> Any:
        ...

    def clear_memory(self) -> None:
        ...

    @property
    def last_prompt(self) -> str:
        ...

    @property
    def last_prompt_id(self) -> str:
        ...

    @property
    def logs(self) -> List:
        ...

    @property
    def logger(self) -> Logger:
        ...

    @logger.setter
    def logger(self, logger: Logger) -> None:
        ...

    @property
    def config(self) -> Config:
        ...

    @property
    def verbose(self) -> bool:
        ...

    @verbose.setter
    def verbose(self, verbose: bool) -> None:
        ...

    @property
    def save_logs(self) -> bool:
        ...

    @save_logs.setter
    def save_logs(self, save_logs: bool) -> None:
        ...

    @property
    def custom_prompts(self) -> dict:
        ...

    @custom_prompts.setter
    def custom_prompts(self, custom_prompts: dict) -> None:
        ...

    @property
    def save_charts(self) -> bool:
        ...

    @save_charts.setter
    def save_charts(self, save_charts: bool) -> None:
        ...

    @property
    def save_charts_path(self) -> str:
        ...

    @save_charts_path.setter
    def save_charts_path(self, save_charts_path: str) -> None:
        ...

    @property
    def last_code_generated(self) -> str:
        ...

    @property
    def last_code_executed(self) -> str:
        ...

    @property
    def last_result(self) -> Any:
        ...

    @property
    def last_error(self) -> str:
        ...

    @property
    def dfs(self) -> List[DataFrame]:
        ...

    @property
    def memory(self) -> Memory:
        ...