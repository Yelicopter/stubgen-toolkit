from google.protobuf import descriptor_pool as _descriptor_pool, message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor_pool.DescriptorPool

class GetPlayerProto(_message.Message):
    FORM_FIELD_NUMBER: ClassVar[int]
    form: GetPlayerProto.Form
    class Form(_message.Message):
        QUERY_FIELD_NUMBER: ClassVar[int]
        query: GetPlayerProto.Form.Query
        class Query(_message.Message):
            ID_FIELD_NUMBER: ClassVar[int]
            id: str
            def __init__(self, id: Optional[str] = ...) -> None: ...
        def __init__(self, query: Optional['GetPlayerProto.Form.Query'] = ...) -> None: ...
    def __init__(self, form: Optional['GetPlayerProto.Form'] = ...) -> None: ...
