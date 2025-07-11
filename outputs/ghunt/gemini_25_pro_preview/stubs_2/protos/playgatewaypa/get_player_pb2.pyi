from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import well_known_types as _well_known_types

class GetPlayerProto(_message.Message):
    class Form(_message.Message):
        class Query(_message.Message):
            id: str
            def __init__(self, id: str = ...) -> None: ...
        query: GetPlayerProto.Form.Query
        def __init__(self, query: GetPlayerProto.Form.Query = ...) -> None: ...
    form: GetPlayerProto.Form
    def __init__(self, form: GetPlayerProto.Form = ...) -> None: ...