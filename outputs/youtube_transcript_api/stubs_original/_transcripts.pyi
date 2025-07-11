from ._errors import AgeRestricted as AgeRestricted, FailedToCreateConsentCookie as FailedToCreateConsentCookie, InvalidVideoId as InvalidVideoId, IpBlocked as IpBlocked, NoTranscriptFound as NoTranscriptFound, NotTranslatable as NotTranslatable, PoTokenRequired as PoTokenRequired, RequestBlocked as RequestBlocked, TranscriptsDisabled as TranscriptsDisabled, TranslationLanguageNotAvailable as TranslationLanguageNotAvailable, VideoUnavailable as VideoUnavailable, VideoUnplayable as VideoUnplayable, YouTubeDataUnparsable as YouTubeDataUnparsable, YouTubeRequestFailed as YouTubeRequestFailed
from ._settings import INNERTUBE_API_URL as INNERTUBE_API_URL, INNERTUBE_CONTEXT as INNERTUBE_CONTEXT, WATCH_URL as WATCH_URL
from .proxies import ProxyConfig as ProxyConfig
from _typeshed import Incomplete
from enum import Enum
from requests import Session
from typing import Dict, Iterable, Iterator, List, Optional

class FetchedTranscriptSnippet:
    text: str
    start: float
    duration: float
    def __init__(self, text, start, duration) -> None: ...

class FetchedTranscript:
    snippets: List[FetchedTranscriptSnippet]
    video_id: str
    language: str
    language_code: str
    is_generated: bool
    def __iter__(self) -> Iterator[FetchedTranscriptSnippet]: ...
    def __getitem__(self, index) -> FetchedTranscriptSnippet: ...
    def __len__(self) -> int: ...
    def to_raw_data(self) -> List[Dict]: ...
    def __init__(self, snippets, video_id, language, language_code, is_generated) -> None: ...

class _TranslationLanguage:
    language: str
    language_code: str
    def __init__(self, language, language_code) -> None: ...

class _PlayabilityStatus(str, Enum):
    OK: str
    ERROR: str
    LOGIN_REQUIRED: str

class _PlayabilityFailedReason(str, Enum):
    BOT_DETECTED: str
    AGE_RESTRICTED: str
    VIDEO_UNAVAILABLE: str

class Transcript:
    video_id: Incomplete
    language: Incomplete
    language_code: Incomplete
    is_generated: Incomplete
    translation_languages: Incomplete
    def __init__(self, http_client: Session, video_id: str, url: str, language: str, language_code: str, is_generated: bool, translation_languages: List[_TranslationLanguage]) -> None: ...
    def fetch(self, preserve_formatting: bool = ...) -> FetchedTranscript: ...
    @property
    def is_translatable(self) -> bool: ...
    def translate(self, language_code: str) -> Transcript: ...

class TranscriptList:
    video_id: Incomplete
    def __init__(self, video_id: str, manually_created_transcripts: Dict[str, Transcript], generated_transcripts: Dict[str, Transcript], translation_languages: List[_TranslationLanguage]) -> None: ...
    @staticmethod
    def build(http_client: Session, video_id: str, captions_json: Dict) -> TranscriptList: ...
    def __iter__(self) -> Iterator[Transcript]: ...
    def find_transcript(self, language_codes: Iterable[str]) -> Transcript: ...
    def find_generated_transcript(self, language_codes: Iterable[str]) -> Transcript: ...
    def find_manually_created_transcript(self, language_codes: Iterable[str]) -> Transcript: ...

class TranscriptListFetcher:
    def __init__(self, http_client: Session, proxy_config: Optional[ProxyConfig]) -> None: ...
    def fetch(self, video_id: str) -> TranscriptList: ...

class _TranscriptParser:
    def __init__(self, preserve_formatting: bool = ...) -> None: ...
    def parse(self, raw_data: str) -> List[FetchedTranscriptSnippet]: ...
