import os
import re
import click

from pandasai import DatasetLoader
from pandasai.data_loader.semantic_layer_schema import (
    SemanticLayerSchema,
    Source,
    SQLConnectionConfig,
)
from pandasai.helpers.path import find_project_root, get_validated_dataset_path

def validate_api_key(api_key: str) -> bool: ...

@click.group()
def cli() -> None: ...

@cli.group()
def dataset() -> None: ...

@dataset.command()
def create() -> None: ...

@cli.command()
@click.argument("api_key")
def login(api_key: str) -> None: ...

@cli.command()
@click.argument("dataset_path")
def pull(dataset_path) -> None: ...

@cli.command()
@click.argument("dataset_path")
def push(dataset_path) -> None: ...