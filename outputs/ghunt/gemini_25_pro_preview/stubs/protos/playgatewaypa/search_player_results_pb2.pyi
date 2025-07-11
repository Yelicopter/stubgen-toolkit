from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import well_known_types as _well_known_types

class PlayerSearchResultsProto(_message.Message):
    class field1_type(_message.Message):
        class Results(_message.Message):
            class field1_type(_message.Message):
                class field1_type(_message.Message):
                    class Player(_message.Message):
                        class Avatar(_message.Message):
                            url: str
                            def __init__(self, url: str = ...) -> None: ...
                        class Account(_message.Message):
                            id: str
                            name: str
                            def __init__(self, id: str = ..., name: str = ...) -> None: ...
                        avatar: PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Avatar
                        account: PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Account
                        def __init__(self, avatar: PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Avatar = ..., account: PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Account = ...) -> None: ...
                    player: _containers.RepeatedCompositeFieldContainer[PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player]
                    def __init__(self, player: _containers.RepeatedCompositeFieldContainer[PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player] = ...) -> None: ...
                field1: PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type
                def __init__(self, field1: PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type = ...) -> None: ...
            field1: PlayerSearchResultsProto.field1_type.Results.field1_type
            def __init__(self, field1: PlayerSearchResultsProto.field1_type.Results.field1_type = ...) -> None: ...
        results: PlayerSearchResultsProto.field1_type.Results
        def __init__(self, results: PlayerSearchResultsProto.field1_type.Results = ...) -> None: ...
    field1: PlayerSearchResultsProto.field1_type
    def __init__(self, field1: PlayerSearchResultsProto.field1_type = ...) -> None: ...