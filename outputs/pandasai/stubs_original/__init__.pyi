from .agent import Agent as Agent
from .dataframe import DataFrame as DataFrame, VirtualDataFrame as VirtualDataFrame
from .smart_dataframe import SmartDataframe as SmartDataframe
from .smart_datalake import SmartDatalake as SmartDatalake
from pandasai.sandbox.sandbox import Sandbox
from typing import Optional

def chat(query: str, *dataframes: DataFrame, sandbox: Optional[Sandbox] = ...): ...
def follow_up(query: str): ...
def load(dataset_path: str) -> DataFrame: ...

# Names in __all__ with no definition:
#   pandas
