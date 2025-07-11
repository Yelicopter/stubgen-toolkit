import os
from fastapi import APIRouter, Query, Request, HTTPException
from pydantic import BaseModel
from evals.utils import image_to_data_url
from evals.config import EVALS_DIR
from typing import Set, List, Dict, Optional, Any
from evals.runner import run_image_evals
from llm import Llm
from prompts.types import Stack
from pathlib import Path

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
    files: List[str] = []

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

@router.get("/eval_input_files", response_model=List[InputFile])
async def get_eval_input_files() -> List[InputFile]: ...

@router.get("/evals", response_model=list[Eval])
async def get_evals(folder: str) -> list[Eval]: ...

@router.get("/pairwise-evals", response_model=PairwiseEvalResponse)
async def get_pairwise_evals(
    folder1: str = Query(..., description="Absolute path to first folder"),
    folder2: str = Query(..., description="Absolute path to second folder"),
) -> PairwiseEvalResponse: ...

@router.post("/run_evals", response_model=List[str])
async def run_evals(request: RunEvalsRequest) -> List[str]: ...

@router.get("/models", response_model=Dict[str, List[str]])
async def get_models() -> Dict[str, List[str]]: ...

@router.get("/best-of-n-evals", response_model=BestOfNEvalsResponse)
async def get_best_of_n_evals(request: Request) -> BestOfNEvalsResponse: ...

@router.get("/output_folders", response_model=List[OutputFolder])
async def get_output_folders() -> List[OutputFolder]: ...