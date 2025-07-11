from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db: _symbol_database.SymbolDatabase
DESCRIPTOR: _descriptor_pool.DescriptorPool

_PLAYERSEARCHPROTO: _descriptor.Descriptor
_PLAYERSEARCHPROTO_SEARCHFORM: _descriptor.Descriptor
_PLAYERSEARCHPROTO_SEARCHFORM_QUERY: _descriptor.Descriptor

class PlayerSearchProto(_message.Message):
    DESCRIPTOR: _descriptor.Descriptor
    
    class SearchForm(_message.Message):
        DESCRIPTOR: _descriptor.Descriptor
        
        class Query(_message.Message):
            DESCRIPTOR: _descriptor.Descriptor
            TEXT_FIELD_NUMBER: int
            text: str
            def __init__(self, *, text: str = ...) -> None: ...
        
        QUERY_FIELD_NUMBER: int
        query: PlayerSearchProto.SearchForm.Query
        def __init__(self, *, query: PlayerSearchProto.SearchForm.Query = ...) -> None: ...
    
    SEARCH_FORM_FIELD_NUMBER: int
    search_form: PlayerSearchProto.SearchForm
    def __init__(self, *, search_form: PlayerSearchProto.SearchForm = ...) -> None: ...