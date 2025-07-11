import argparse
from typing import List, Any
from .proxies import GenericProxyConfig, WebshareProxyConfig
from .formatters import FormatterLoader
from ._api import YouTubeTranscriptApi, FetchedTranscript, TranscriptList

class YouTubeTranscriptCli:
    def __init__(self, args: List[str]) -> None:
        ...

    def run(self) -> str:
        ...

    def _fetch_transcript(
        self,
        parsed_args: Any,
        transcript_list: TranscriptList,
    ) -> FetchedTranscript:
        ...

    def _parse_args(self) -> Any:
        ...

    def _sanitize_video_ids(self, args: Any) -> Any:
        ...