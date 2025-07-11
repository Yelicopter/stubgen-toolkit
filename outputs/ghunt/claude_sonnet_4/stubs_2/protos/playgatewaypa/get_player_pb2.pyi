from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

_sym_db: _symbol_database.SymbolDatabase
DESCRIPTOR: _descriptor_pool.DescriptorPool

_GETPLAYERPROTO: _descriptor.Descriptor
_GETPLAYERPROTO_FORM: _descriptor.Descriptor
_GETPLAYERPROTO_FORM_QUERY: _descriptor.Descriptor

class GetPlayerProto(_message.Message):
    DESCRIPTOR: _descriptor.Descriptor
    
    class Form(_message.Message):
        DESCRIPTOR: _descriptor.Descriptor
        
        class Query(_message.Message):
            DESCRIPTOR: _descriptor.Descriptor
            ID_FIELD_NUMBER: int
            id: str
            def __init__(self, *, id: str = ...) -> None: ...
        
        QUERY_FIELD_NUMBER: int
        query: GetPlayerProto.Form.Query
        def __init__(self, *, query: GetPlayerProto.Form.Query = ...) -> None: ...
    
    FORM_FIELD_NUMBER: int
    form: GetPlayerProto.Form
    def __init__(self, *, form: GetPlayerProto.Form = ...) -> None: ...