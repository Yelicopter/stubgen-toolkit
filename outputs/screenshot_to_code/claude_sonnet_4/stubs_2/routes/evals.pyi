from fastapi import APIRouter, Query, Request, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from llm import Llm
from prompts.types import Stack

router: APIRouter

class Eval(BaseModel):
    input: str
    outputs: List[str]

class InputFile(BaseModel):
    name: str
    path: str

class PairwiseEvalResponse(BaseModel):
    evals: List[Eval]
    folder1_name: str
    folder2_name: str

class RunEvalsRequest(BaseModel):
    models: List[str]
    stack: Stack
    files: List[str]

class BestOfNEvalsResponse(BaseModel):
    evals: List[Eval]
    folder_names: List[str]

class OutputFolder(BaseModel):
    name: str
    path: str
    modified_time: float

async def get_eval_input_files() -> List[InputFile]: ...
async def get_evals(folder: str) -> List[Eval]: ...
async def get_pairwise_evals(
    folder1: str = Query(...),
    folder2: str = Query(...),
) -> PairwiseEvalResponse: ...
async def run_evals(request: RunEvalsRequest) -> List[str]: ...
async def get_models() -> Dict[str, List[str]]: ...
async def get_best_of_n_evals(request: Request) -> BestOfNEvalsResponse: ...
async def get_output_folders() -> List[OutputFolder]: ...