from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import well_known_types as _well_known_types

class PlayerSearchProto(_message.Message):
    class SearchForm(_message.Message):
        class Query(_message.Message):
            text: str
            def __init__(self, text: str = ...) -> None: ...
        query: PlayerSearchProto.SearchForm.Query
        def __init__(self, query: PlayerSearchProto.SearchForm.Query = ...) -> None: ...
    search_form: PlayerSearchProto.SearchForm
    def __init__(self, search_form: PlayerSearchProto.SearchForm = ...) -> None: ...