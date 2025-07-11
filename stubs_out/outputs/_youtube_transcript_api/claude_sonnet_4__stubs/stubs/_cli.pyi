from ._api import FetchedTranscript as FetchedTranscript, TranscriptList as TranscriptList, YouTubeTranscriptApi as YouTubeTranscriptApi
from .formatters import FormatterLoader as FormatterLoader
from .proxies import GenericProxyConfig as GenericProxyConfig, WebshareProxyConfig as WebshareProxyConfig
from typing import List

class YouTubeTranscriptCli:
    def __init__(self, args: List[str]) -> None: ...
    def run(self) -> str: ...
