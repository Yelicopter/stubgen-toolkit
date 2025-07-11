from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor_pool.DescriptorPool

class GetPlayerProto(_message.Message):
    __slots__ = ["form"]
    FORM_FIELD_NUMBER: ClassVar[int]
    form: "GetPlayerProto.Form"
    
    class Form(_message.Message):
        __slots__ = ["query"]
        QUERY_FIELD_NUMBER: ClassVar[int]
        query: "GetPlayerProto.Form.Query"
        
        class Query(_message.Message):
            __slots__ = ["id"]
            ID_FIELD_NUMBER: ClassVar[int]
            id: str
            def __init__(self, id: Optional[str] = ...) -> None: ...
        
        def __init__(self, query: Optional["GetPlayerProto.Form.Query"] = ...) -> None: ...
    
    def __init__(self, form: Optional["GetPlayerProto.Form"] = ...) -> None: ...