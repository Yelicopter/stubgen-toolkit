from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from typing import ClassVar, Optional, List

DESCRIPTOR: _descriptor_pool.DescriptorPool

class PlayerSearchResultsProto(_message.Message):
    __slots__ = ["field1"]
    FIELD1_FIELD_NUMBER: ClassVar[int]
    field1: "PlayerSearchResultsProto.field1_type"
    
    class field1_type(_message.Message):
        __slots__ = ["results"]
        RESULTS_FIELD_NUMBER: ClassVar[int]
        results: "PlayerSearchResultsProto.field1_type.Results"
        
        class Results(_message.Message):
            __slots__ = ["field1"]
            FIELD1_FIELD_NUMBER: ClassVar[int]
            field1: "PlayerSearchResultsProto.field1_type.Results.field1_type"
            
            class field1_type(_message.Message):
                __slots__ = ["field1"]
                FIELD1_FIELD_NUMBER: ClassVar[int]
                field1: "PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type"
                
                class field1_type(_message.Message):
                    __slots__ = ["player"]
                    PLAYER_FIELD_NUMBER: ClassVar[int]
                    player: List["PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player"]
                    
                    class Player(_message.Message):
                        __slots__ = ["avatar", "account"]
                        AVATAR_FIELD_NUMBER: ClassVar[int]
                        ACCOUNT_FIELD_NUMBER: ClassVar[int]
                        avatar: "PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Avatar"
                        account: "PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Account"
                        
                        class Avatar(_message.Message):
                            __slots__ = ["url"]
                            URL_FIELD_NUMBER: ClassVar[int]
                            url: str
                            def __init__(self, url: Optional[str] = ...) -> None: ...
                        
                        class Account(_message.Message):
                            __slots__ = ["id", "name"]
                            ID_FIELD_NUMBER: ClassVar[int]
                            NAME_FIELD_NUMBER: ClassVar[int]
                            id: str
                            name: str
                            def __init__(self, id: Optional[str] = ..., name: Optional[str] = ...) -> None: ...
                        
                        def __init__(self, avatar: Optional["PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Avatar"] = ..., account: Optional["PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player.Account"] = ...) -> None: ...
                    
                    def __init__(self, player: Optional[List["PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type.Player"]] = ...) -> None: ...
                
                def __init__(self, field1: Optional["PlayerSearchResultsProto.field1_type.Results.field1_type.field1_type"] = ...) -> None: ...
            
            def __init__(self, field1: Optional["PlayerSearchResultsProto.field1_type.Results.field1_type"] = ...) -> None: ...
        
        def __init__(self, results: Optional["PlayerSearchResultsProto.field1_type.Results"] = ...) -> None: ...
    
    def __init__(self, field1: Optional["PlayerSearchResultsProto.field1_type"] = ...) -> None: ...