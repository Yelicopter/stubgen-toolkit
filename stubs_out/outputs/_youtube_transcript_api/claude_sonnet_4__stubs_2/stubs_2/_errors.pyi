from ._settings import WATCH_URL as WATCH_URL
from .proxies import GenericProxyConfig as GenericProxyConfig, ProxyConfig as ProxyConfig, WebshareProxyConfig as WebshareProxyConfig
from pathlib import Path
from requests import HTTPError
from typing import Any, Iterable, List, Optional

class YouTubeTranscriptApiException(Exception): ...
class CookieError(YouTubeTranscriptApiException): ...

class CookiePathInvalid(CookieError):
    def __init__(self, cookie_path: Path) -> None: ...

class CookieInvalid(CookieError):
    def __init__(self, cookie_path: Path) -> None: ...

class CouldNotRetrieveTranscript(YouTubeTranscriptApiException):
    ERROR_MESSAGE: str
    CAUSE_MESSAGE_INTRO: str
    CAUSE_MESSAGE: str
    GITHUB_REFERRAL: str
    def __init__(self, video_id: str) -> None: ...
    @property
    def cause(self) -> str: ...

class YouTubeDataUnparsable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class YouTubeRequestFailed(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str
    def __init__(self, video_id: str, http_error: HTTPError) -> None: ...
    @property
    def cause(self) -> str: ...

class VideoUnplayable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str
    SUBREASON_MESSAGE: str
    def __init__(self, video_id: str, reason: Optional[str], sub_reasons: List[str]) -> None: ...
    @property
    def cause(self) -> str: ...

class VideoUnavailable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class InvalidVideoId(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class RequestBlocked(CouldNotRetrieveTranscript):
    BASE_CAUSE_MESSAGE: str
    CAUSE_MESSAGE: str
    WITH_GENERIC_PROXY_CAUSE_MESSAGE: str
    WITH_WEBSHARE_PROXY_CAUSE_MESSAGE: str
    def __init__(self, video_id: str) -> None: ...
    def with_proxy_config(self, proxy_config: Optional[ProxyConfig]) -> RequestBlocked: ...
    @property
    def cause(self) -> str: ...

class IpBlocked(RequestBlocked):
    CAUSE_MESSAGE: str

class TranscriptsDisabled(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class AgeRestricted(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class NotTranslatable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class TranslationLanguageNotAvailable(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class FailedToCreateConsentCookie(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str

class NoTranscriptFound(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str
    def __init__(self, video_id: str, requested_language_codes: Iterable[str], transcript_data: Any) -> None: ...
    @property
    def cause(self) -> str: ...

class PoTokenRequired(CouldNotRetrieveTranscript):
    CAUSE_MESSAGE: str
