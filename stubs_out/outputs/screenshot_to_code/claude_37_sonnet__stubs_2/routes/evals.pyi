from evals.config import EVALS_DIR as EVALS_DIR
from evals.runner import run_image_evals as run_image_evals
from evals.utils import image_to_data_url as image_to_data_url
from fastapi import APIRouter as APIRouter, HTTPException as HTTPException, Request as Request
from llm import Llm as Llm
from pathlib import Path as Path
from prompts.types import Stack as Stack
from pydantic import BaseModel
from typing import Dict, List

router: APIRouter

class Eval(BaseModel):
    input: str
    outputs: list[str]

class InputFile(BaseModel):
    name: str
    path: str

class RunEvalsRequest(BaseModel):
    models: List[str]
    stack: Stack
    files: List[str]

class BestOfNEvalsResponse(BaseModel):
    evals: list[Eval]
    folder_names: list[str]

class OutputFolder(BaseModel):
    name: str
    path: str
    modified_time: float

class PairwiseEvalResponse(BaseModel):
    evals: list[Eval]
    folder1_name: str
    folder2_name: str

async def get_eval_input_files() -> List[InputFile]: ...
async def get_evals(folder: str) -> list[Eval]: ...
async def get_pairwise_evals(folder1: str = ..., folder2: str = ...) -> PairwiseEvalResponse: ...
async def run_evals(request: RunEvalsRequest) -> List[str]: ...
async def get_models() -> Dict[str, List[str]]: ...
async def get_best_of_n_evals(request: Request) -> BestOfNEvalsResponse: ...
async def get_output_folders() -> List[OutputFolder]: ...
