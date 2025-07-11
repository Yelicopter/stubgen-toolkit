from pathlib import Path
from typing import Iterable, Optional, List

from requests import HTTPError

from ._settings import WATCH_URL
from .proxies import ProxyConfig, GenericProxyConfig, WebshareProxyConfig

class YouTubeTranscriptApiException(Exception):
    pass

class CookieError(YouTubeTranscriptApiException):
    pass

class CookiePathInvalid(CookieError):
    def __init__(self, cookie_path: Path) -> None:
        ...

class CookieInvalid(CookieError):
    def __init__(self, cookie_path: Path) -> None:
        ...

class CouldNotRetrieveTranscript(YouTubeTranscriptApiException):
    ...

class YouTubeDataUnparsable(CouldNotRetrieveTranscript):
    ...

class YouTubeRequestFailed(CouldNotRetrieveTranscript):
    ...

class VideoUnplayable(CouldNotRetrieveTranscript):
    ...

class VideoUnavailable(CouldNotRetrieveTranscript):
    ...

class InvalidVideoId(CouldNotRetrieveTranscript):
    ...

class RequestBlocked(CouldNotRetrieveTranscript):
    ...

class IpBlocked(RequestBlocked):
    ...

class TranscriptsDisabled(CouldNotRetrieveTranscript):
    ...

class AgeRestricted(CouldNotRetrieveTranscript):
    ...

class NotTranslatable(CouldNotRetrieveTranscript):
    ...

class TranslationLanguageNotAvailable(CouldNotRetrieveTranscript):
    ...

class FailedToCreateConsentCookie(CouldNotRetrieveTranscript):
    ...

class NoTranscriptFound(CouldNotRetrieveTranscript):
    ...

class PoTokenRequired(CouldNotRetrieveTranscript):
    ...