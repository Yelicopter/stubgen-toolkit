import argparse
from typing import List, Optional, Any

from .proxies import GenericProxyConfig, WebshareProxyConfig
from .formatters import FormatterLoader
from ._transcripts import FetchedTranscript, TranscriptList
from ._api import YouTubeTranscriptApi

class YouTubeTranscriptCli:
    def __init__(self, args: List[str]) -> None: ...
    
    def run(self) -> str: ...
    
    def _fetch_transcript(
        self,
        parsed_args: argparse.Namespace,
        transcript_list: TranscriptList,
    ) -> FetchedTranscript: ...
    
    def _parse_args(self) -> argparse.Namespace: ...
    
    def _sanitize_video_ids(self, args: argparse.Namespace) -> argparse.Namespace: ...