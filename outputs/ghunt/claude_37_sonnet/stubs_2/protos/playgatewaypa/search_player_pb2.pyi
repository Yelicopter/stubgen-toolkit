from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor_pool.DescriptorPool

class PlayerSearchProto(_message.Message):
    __slots__ = ["search_form"]
    SEARCH_FORM_FIELD_NUMBER: ClassVar[int]
    search_form: "PlayerSearchProto.SearchForm"
    
    class SearchForm(_message.Message):
        __slots__ = ["query"]
        QUERY_FIELD_NUMBER: ClassVar[int]
        query: "PlayerSearchProto.SearchForm.Query"
        
        class Query(_message.Message):
            __slots__ = ["text"]
            TEXT_FIELD_NUMBER: ClassVar[int]
            text: str
            def __init__(self, text: Optional[str] = ...) -> None: ...
        
        def __init__(self, query: Optional["PlayerSearchProto.SearchForm.Query"] = ...) -> None: ...
    
    def __init__(self, search_form: Optional["PlayerSearchProto.SearchForm"] = ...) -> None: ...