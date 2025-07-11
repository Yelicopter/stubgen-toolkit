from google.protobuf import descriptor_pool as _descriptor_pool, message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor_pool.DescriptorPool

class PlayerSearchProto(_message.Message):
    SEARCH_FORM_FIELD_NUMBER: ClassVar[int]
    search_form: PlayerSearchProto.SearchForm
    class SearchForm(_message.Message):
        QUERY_FIELD_NUMBER: ClassVar[int]
        query: PlayerSearchProto.SearchForm.Query
        class Query(_message.Message):
            TEXT_FIELD_NUMBER: ClassVar[int]
            text: str
            def __init__(self, text: Optional[str] = ...) -> None: ...
        def __init__(self, query: Optional['PlayerSearchProto.SearchForm.Query'] = ...) -> None: ...
    def __init__(self, search_form: Optional['PlayerSearchProto.SearchForm'] = ...) -> None: ...
