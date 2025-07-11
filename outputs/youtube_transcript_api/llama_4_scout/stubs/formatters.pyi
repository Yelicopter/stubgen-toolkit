import json
from typing import List, Iterable

from ._transcripts import FetchedTranscript, FetchedTranscriptSnippet

class Formatter:
    def format_transcript(self, transcript: FetchedTranscript, **kwargs) -> str:
        ...

    def format_transcripts(self, transcripts: Iterable[FetchedTranscript], **kwargs) -> str:
        ...

class PrettyPrintFormatter(Formatter):
    ...

class JSONFormatter(Formatter):
    ...

class TextFormatter(Formatter):
    ...

class _TextBasedFormatter(TextFormatter):
    ...

class SRTFormatter(_TextBasedFormatter):
    ...

class WebVTTFormatter(_TextBasedFormatter):
    ...

class FormatterLoader:
    TYPES = {
        "json": JSONFormatter,
        "pretty": PrettyPrintFormatter,
        "text": TextFormatter,
        "webvtt": WebVTTFormatter,
        "srt": SRTFormatter,
    }

    def load(self, formatter_type: str = "pretty") -> Formatter:
        ...