import uuid
import warnings
from functools import cached_property
from io import StringIO
from typing import Any, List, Optional, Union

import pandas as pd

from pandasai.agent import Agent
from pandasai.dataframe import DataFrame

class SmartDataframe:
    _table_name: str
    _table_description: str
    _custom_head: str | None
    _original_import: Any

    def __init__(
        self,
        df: pd.DataFrame,
        name: str | None = None,
        description: str | None = None,
        custom_head: pd.DataFrame | None = None,
        config: Config | None = None,
    ) -> None:
        ...

    def load_df(
        self, df: pd.DataFrame, name: str | None, description: str | None, custom_head: pd.DataFrame | None
    ) -> DataFrame:
        ...

    def chat(self, query: str, output_type: str | None = None) -> Any:
        ...

    @cached_property
    def head_df(self) -> pd.DataFrame:
        ...

    @cached_property
    def head_csv(self) -> str:
        ...

    @property
    def last_prompt(self) -> str:
        ...

    @property
    def last_prompt_id(self) -> str:
        ...

    @property
    def last_code_generated(self) -> str:
        ...

    @property
    def last_code_executed(self) -> str:
        ...

    def original_import(self) -> Any:
        ...

    @property
    def logger(self) -> Logger:
        ...

    @logger.setter
    def logger(self, logger: Logger) -> None:
        ...

    @property
    def logs(self) -> List:
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
    def table_name(self) -> str:
        ...

    @property
    def table_description(self) -> str:
        ...

    @property
    def custom_head(self) -> pd.DataFrame:
        ...

    def __len__(self) -> int:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __getattr__(self, name: str) -> Any:
        ...

    def __getitem__(self, key: Any) -> Any:
        ...

    def __setitem__(self, key: Any, value: Any) -> None:
        ...