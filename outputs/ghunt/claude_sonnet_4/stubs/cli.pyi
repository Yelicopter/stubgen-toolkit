from rich_argparse import RichHelpFormatter
import argparse
from typing import *
import sys
from pathlib import Path

def parse_and_run() -> None: ...
def process_args(args: argparse.Namespace) -> None: ...