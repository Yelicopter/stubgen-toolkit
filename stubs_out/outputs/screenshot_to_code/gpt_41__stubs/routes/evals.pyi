from fastapi import APIRouter as APIRouter, HTTPException as HTTPException, Query as Query, Request as Request
from prompts.types import Stack as Stack
from pydantic import BaseModel
from typing import Any, Dict, List

router: APIRouter

class Eval(BaseModel):
    input: str
    outputs: List[str]

class InputFile(BaseModel):
    name: str
    path: str

async def get_eval_input_files() -> List[InputFile]: ...
async def get_evals(folder: str) -> List[Eval]: ...

class PairwiseEvalResponse(BaseModel):
    evals: List[Eval]
    folder1_name: str
    folder2_name: str

async def get_pairwise_evals(folder1: str = ..., folder2: str = ...) -> PairwiseEvalResponse: ...

class RunEvalsRequest(BaseModel):
    models: List[str]
    stack: Stack
    files: List[str]

async def run_evals(request: RunEvalsRequest) -> List[str]: ...
async def get_models() -> Dict[str, List[str]]: ...

class BestOfNEvalsResponse(BaseModel):
    evals: List[Eval]
    folder_names: List[str]

async def get_best_of_n_evals(request: Any) -> BestOfNEvalsResponse: ...

class OutputFolder(BaseModel):
    name: str
    path: str
    modified_time: float

async def get_output_folders() -> List[OutputFolder]: ...
