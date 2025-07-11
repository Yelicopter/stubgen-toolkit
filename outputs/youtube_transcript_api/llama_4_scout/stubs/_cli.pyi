import argparse
from typing import List

from .proxies import GenericProxyConfig, WebshareProxyConfig
from .formatters import FormatterLoader

from ._api import YouTubeTranscriptApi, FetchedTranscript, TranscriptList

class YouTubeTranscriptCli:
    def __init__(self, args: List[str]) -> None:
        ...

    def run(self) -> str:
        ...