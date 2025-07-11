from google.protobuf import descriptor as _descriptor, descriptor_pool as _descriptor_pool, message as _message

DESCRIPTOR: _descriptor_pool.DescriptorPool

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
