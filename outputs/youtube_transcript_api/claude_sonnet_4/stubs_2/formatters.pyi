import json
import pprint
from typing import List, Iterable, Any, Dict, Type
from ._transcripts import FetchedTranscript, FetchedTranscriptSnippet

class Formatter:
    def format_transcript(self, transcript: FetchedTranscript, **kwargs: Any) -> str:
        ...

    def format_transcripts(self, transcripts: List[FetchedTranscript], **kwargs: Any) -> str:
        ...

class PrettyPrintFormatter(Formatter):
    def format_transcript(self, transcript: FetchedTranscript, **kwargs: Any) -> str:
        ...

    def format_transcripts(self, transcripts: List[FetchedTranscript], **kwargs: Any) -> str:
        ...

class JSONFormatter(Formatter):
    def format_transcript(self, transcript: FetchedTranscript, **kwargs: Any) -> str:
        ...

    def format_transcripts(self, transcripts: List[FetchedTranscript], **kwargs: Any) -> str:
        ...

class TextFormatter(Formatter):
    def format_transcript(self, transcript: FetchedTranscript, **kwargs: Any) -> str:
        ...

    def format_transcripts(self, transcripts: List[FetchedTranscript], **kwargs: Any) -> str:
        ...

class _TextBasedFormatter(TextFormatter):
    def _format_timestamp(self, hours: int, mins: int, secs: int, ms: int) -> str:
        ...

    def _format_transcript_header(self, lines: List[str]) -> str:
        ...

    def _format_transcript_helper(
        self, i: int, time_text: str, snippet: FetchedTranscriptSnippet
    ) -> str:
        ...

    def _seconds_to_timestamp(self, time: float) -> str:
        ...

    def format_transcript(self, transcript: FetchedTranscript, **kwargs: Any) -> str:
        ...

class SRTFormatter(_TextBasedFormatter):
    def _format_timestamp(self, hours: int, mins: int, secs: int, ms: int) -> str:
        ...

    def _format_transcript_header(self, lines: List[str]) -> str:
        ...

    def _format_transcript_helper(
        self, i: int, time_text: str, snippet: FetchedTranscriptSnippet
    ) -> str:
        ...

class WebVTTFormatter(_TextBasedFormatter):
    def _format_timestamp(self, hours: int, mins: int, secs: int, ms: int) -> str:
        ...

    def _format_transcript_header(self, lines: List[str]) -> str:
        ...

    def _format_transcript_helper(
        self, i: int, time_text: str, snippet: FetchedTranscriptSnippet
    ) -> str:
        ...

class FormatterLoader:
    TYPES: Dict[str, Type[Formatter]]

    class UnknownFormatterType(Exception):
        def __init__(self, formatter_type: str) -> None:
            ...

    def load(self, formatter_type: str = "pretty") -> Formatter:
        ...