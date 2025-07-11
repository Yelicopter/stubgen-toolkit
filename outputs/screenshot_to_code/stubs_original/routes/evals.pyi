from _typeshed import Incomplete
from fastapi import Request as Request
from prompts.types import Stack
from pydantic import BaseModel
from typing import List

router: Incomplete
N: int

class Eval(BaseModel):
    input: str
    outputs: list[str]

class InputFile(BaseModel):
    name: str
    path: str

async def get_eval_input_files(): ...
async def get_evals(folder: str): ...

class PairwiseEvalResponse(BaseModel):
    evals: list[Eval]
    folder1_name: str
    folder2_name: str

async def get_pairwise_evals(folder1: str = ..., folder2: str = ...): ...

class RunEvalsRequest(BaseModel):
    models: List[str]
    stack: Stack
    files: List[str]

async def run_evals(request: RunEvalsRequest) -> List[str]: ...
async def get_models(): ...

class BestOfNEvalsResponse(BaseModel):
    evals: list[Eval]
    folder_names: list[str]

async def get_best_of_n_evals(request: Request): ...

class OutputFolder(BaseModel):
    name: str
    path: str
    modified_time: float

async def get_output_folders(): ...
