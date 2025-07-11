from typing import *
import argparse
from pathlib import Path as Path
from rich_argparse import RichHelpFormatter as RichHelpFormatter

def parse_and_run() -> None: ...
def process_args(args: argparse.Namespace) -> None: ...
