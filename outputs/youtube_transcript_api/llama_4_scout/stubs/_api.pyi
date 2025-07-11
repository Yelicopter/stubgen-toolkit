import warnings
from typing import Optional, Iterable

from requests import Session

from .proxies import ProxyConfig, GenericProxyConfig

from ._transcripts import TranscriptListFetcher, FetchedTranscript, TranscriptList

class YouTubeTranscriptApi:
    def __init__(
        self,
        proxy_config: Optional[ProxyConfig] = None,
        http_client: Optional[Session] = None,
    ) -> None:
        ...

    def fetch(
        self,
        video_id: str,
        languages: Iterable[str] = ("en",),
        preserve_formatting: bool = False,
    ) -> FetchedTranscript:
        ...

    def list(
        self,
        video_id: str,
    ) -> TranscriptList:
        ...

    @classmethod
    def list_transcripts(cls, video_id: str, proxies: Optional[dict] = None) -> TranscriptList:
        ...

    @classmethod
    def get_transcripts(
        cls,
        video_ids: list[str],
        languages: Iterable[str] = ("en",),
        continue_after_error: bool = False,
        proxies: Optional[dict] = None,
        preserve_formatting: bool = False,
    ) -> tuple[dict[str, list[dict]], list[str]]:
        ...

    @classmethod
    def get_transcript(
        cls,
        video_id: str,
        languages: Iterable[str] = ("en",),
        proxies: Optional[dict] = None,
        preserve_formatting: bool = False,
    ) -> list[dict]:
        ...