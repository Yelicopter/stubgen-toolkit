from google.protobuf import descriptor as _descriptor, descriptor_pool as _descriptor_pool, message as _message

DESCRIPTOR: _descriptor_pool.DescriptorPool

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
