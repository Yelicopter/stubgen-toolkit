from dataclasses import dataclass, asdict
from enum import Enum
from itertools import chain
from html import unescape
from typing import List, Dict, Iterator, Iterable, Pattern, Optional, Any
from defusedxml import ElementTree
import re
from requests import HTTPError, Session, Response
from .proxies import ProxyConfig
from ._settings import WATCH_URL, INNERTUBE_CONTEXT, INNERTUBE_API_URL
from ._errors import (
    VideoUnavailable,
    YouTubeRequestFailed,
    NoTranscriptFound,
    TranscriptsDisabled,
    NotTranslatable,
    TranslationLanguageNotAvailable,
    FailedToCreateConsentCookie,
    InvalidVideoId,
    IpBlocked,
    RequestBlocked,
    AgeRestricted,
    VideoUnplayable,
    YouTubeDataUnparsable,
    PoTokenRequired,
)

@dataclass
class FetchedTranscriptSnippet:
    text: str
    start: float
    duration: float

@dataclass
class FetchedTranscript:
    snippets: List[FetchedTranscriptSnippet]
    video_id: str
    language: str
    language_code: str
    is_generated: bool

    def __iter__(self) -> Iterator[FetchedTranscriptSnippet]:
        ...

    def __getitem__(self, index: int) -> FetchedTranscriptSnippet:
        ...

    def __len__(self) -> int:
        ...

    def to_raw_data(self) -> List[Dict[str, Any]]:
        ...

@dataclass
class _TranslationLanguage:
    language: str
    language_code: str

class _PlayabilityStatus(str, Enum):
    OK = "OK"
    ERROR = "ERROR"
    LOGIN_REQUIRED = "LOGIN_REQUIRED"

class _PlayabilityFailedReason(str, Enum):
    BOT_DETECTED = "BOT_DETECTED"
    AGE_RESTRICTED = "AGE_RESTRICTED"
    VIDEO_UNAVAILABLE = "VIDEO_UNAVAILABLE"

def _raise_http_errors(response: Response, video_id: str) -> Response:
    ...

class Transcript:
    def __init__(
        self,
        http_client: Session,
        video_id: str,
        url: str,
        language: str,
        language_code: str,
        is_generated: bool,
        translation_languages: List[_TranslationLanguage],
    ) -> None:
        ...

    def fetch(self, preserve_formatting: bool = False) -> FetchedTranscript:
        ...

    def __str__(self) -> str:
        ...

    @property
    def is_translatable(self) -> bool:
        ...

    def translate(self, language_code: str) -> "Transcript":
        ...

class TranscriptList:
    def __init__(
        self,
        video_id: str,
        manually_created_transcripts: Dict[str, Transcript],
        generated_transcripts: Dict[str, Transcript],
        translation_languages: List[_TranslationLanguage],
    ) -> None:
        ...

    @staticmethod
    def build(
        http_client: Session, video_id: str, captions_json: Dict[str, Any]
    ) -> "TranscriptList":
        ...

    def __iter__(self) -> Iterator[Transcript]:
        ...

    def find_transcript(self, language_codes: Iterable[str]) -> Transcript:
        ...

    def find_generated_transcript(self, language_codes: Iterable[str]) -> Transcript:
        ...

    def find_manually_created_transcript(
        self, language_codes: Iterable[str]
    ) -> Transcript:
        ...

    def _find_transcript(
        self,
        language_codes: Iterable[str],
        transcript_dicts: List[Dict[str, Transcript]],
    ) -> Transcript:
        ...

    def __str__(self) -> str:
        ...

    def _get_language_description(self, transcript_strings: Iterable[str]) -> str:
        ...

class TranscriptListFetcher:
    def __init__(self, http_client: Session, proxy_config: Optional[ProxyConfig]) -> None:
        ...

    def fetch(self, video_id: str) -> TranscriptList:
        ...

    def _fetch_captions_json(self, video_id: str, try_number: int = 0) -> Dict[str, Any]:
        ...

    def _extract_innertube_api_key(self, html: str, video_id: str) -> str:
        ...

    def _extract_captions_json(self, innertube_data: Dict[str, Any], video_id: str) -> Dict[str, Any]:
        ...

    def _assert_playability(self, playability_status_data: Dict[str, Any], video_id: str) -> None:
        ...

    def _create_consent_cookie(self, html: str, video_id: str) -> None:
        ...

    def _fetch_video_html(self, video_id: str) -> str:
        ...

    def _fetch_html(self, video_id: str) -> str:
        ...

    def _fetch_innertube_data(self, video_id: str, api_key: str) -> Dict[str, Any]:
        ...

class _TranscriptParser:
    _FORMATTING_TAGS: List[str]

    def __init__(self, preserve_formatting: bool = False) -> None:
        ...

    def _get_html_regex(self, preserve_formatting: bool) -> Pattern[str]:
        ...

    def parse(self, raw_data: str) -> List[FetchedTranscriptSnippet]:
        ...