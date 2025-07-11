from google.protobuf import message as _message

class GetPlayerProto(_message.Message):
    class Form(_message.Message):
        class Query(_message.Message):
            id: str
            def __init__(self, id: str = ...) -> None: ...
        query: GetPlayerProto.Form.Query
        def __init__(self, query: GetPlayerProto.Form.Query = ...) -> None: ...
    form: GetPlayerProto.Form
    def __init__(self, form: GetPlayerProto.Form = ...) -> None: ...
