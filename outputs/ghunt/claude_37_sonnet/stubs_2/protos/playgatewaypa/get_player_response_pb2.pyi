from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor_pool.DescriptorPool

class GetPlayerResponseProto(_message.Message):
    __slots__ = ["field1"]
    FIELD1_FIELD_NUMBER: ClassVar[int]
    field1: "GetPlayerResponseProto.field1_type"
    
    class field1_type(_message.Message):
        __slots__ = ["results"]
        RESULTS_FIELD_NUMBER: ClassVar[int]
        results: "GetPlayerResponseProto.field1_type.Results"
        
        class Results(_message.Message):
            __slots__ = ["player", "section"]
            PLAYER_FIELD_NUMBER: ClassVar[int]
            SECTION_FIELD_NUMBER: ClassVar[int]
            player: "GetPlayerResponseProto.field1_type.Results.Player"
            section: list["GetPlayerResponseProto.field1_type.Results.Section"]
            
            class Player(_message.Message):
                __slots__ = ["field1", "avatar"]
                FIELD1_FIELD_NUMBER: ClassVar[int]
                AVATAR_FIELD_NUMBER: ClassVar[int]
                field1: "GetPlayerResponseProto.field1_type.Results.Player.field1_type"
                avatar: "GetPlayerResponseProto.field1_type.Results.Player.Avatar"
                
                class field1_type(_message.Message):
                    __slots__ = ["name"]
                    NAME_FIELD_NUMBER: ClassVar[int]
                    name: str
                    def __init__(self, name: Optional[str] = ...) -> None: ...
                
                class Avatar(_message.Message):
                    __slots__ = ["url"]
                    URL_FIELD_NUMBER: ClassVar[int]
                    url: str
                    def __init__(self, url: Optional[str] = ...) -> None: ...
                
                def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Player.field1_type"] = ..., avatar: Optional["GetPlayerResponseProto.field1_type.Results.Player.Avatar"] = ...) -> None: ...
            
            class Section(_message.Message):
                __slots__ = ["counter", "field3", "played_games", "achievements"]
                COUNTER_FIELD_NUMBER: ClassVar[int]
                FIELD3_FIELD_NUMBER: ClassVar[int]
                PLAYED_GAMES_FIELD_NUMBER: ClassVar[int]
                ACHIEVEMENTS_FIELD_NUMBER: ClassVar[int]
                counter: "GetPlayerResponseProto.field1_type.Results.Section.Counter"
                field3: "GetPlayerResponseProto.field1_type.Results.Section.field3_type"
                played_games: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames"
                achievements: "GetPlayerResponseProto.field1_type.Results.Section.Achievements"
                
                class Counter(_message.Message):
                    __slots__ = ["number"]
                    NUMBER_FIELD_NUMBER: ClassVar[int]
                    number: str
                    def __init__(self, number: Optional[str] = ...) -> None: ...
                
                class field3_type(_message.Message):
                    __slots__ = ["section_name"]
                    SECTION_NAME_FIELD_NUMBER: ClassVar[int]
                    section_name: str
                    def __init__(self, section_name: Optional[str] = ...) -> None: ...
                
                class PlayedGames(_message.Message):
                    __slots__ = ["field1"]
                    FIELD1_FIELD_NUMBER: ClassVar[int]
                    field1: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type"
                    
                    class field1_type(_message.Message):
                        __slots__ = ["field1", "game", "field234686954"]
                        FIELD1_FIELD_NUMBER: ClassVar[int]
                        GAME_FIELD_NUMBER: ClassVar[int]
                        FIELD234686954_FIELD_NUMBER: ClassVar[int]
                        field1: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type"
                        game: list["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game"]
                        field234686954: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type"
                        
                        class field1_type(_message.Message):
                            __slots__ = ["field203130867"]
                            FIELD203130867_FIELD_NUMBER: ClassVar[int]
                            field203130867: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type.field203130867_type"
                            
                            class field203130867_type(_message.Message):
                                __slots__ = ["field1"]
                                FIELD1_FIELD_NUMBER: ClassVar[int]
                                field1: str
                                def __init__(self, field1: Optional[str] = ...) -> None: ...
                            
                            def __init__(self, field203130867: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type.field203130867_type"] = ...) -> None: ...
                        
                        class Game(_message.Message):
                            __slots__ = ["icon", "field6"]
                            ICON_FIELD_NUMBER: ClassVar[int]
                            FIELD6_FIELD_NUMBER: ClassVar[int]
                            icon: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.Icon"
                            field6: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type"
                            
                            class Icon(_message.Message):
                                __slots__ = ["url"]
                                URL_FIELD_NUMBER: ClassVar[int]
                                url: str
                                def __init__(self, url: Optional[str] = ...) -> None: ...
                            
                            class field6_type(_message.Message):
                                __slots__ = ["field1"]
                                FIELD1_FIELD_NUMBER: ClassVar[int]
                                field1: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type"
                                
                                class field1_type(_message.Message):
                                    __slots__ = ["details"]
                                    DETAILS_FIELD_NUMBER: ClassVar[int]
                                    details: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details"
                                    
                                    class Details(_message.Message):
                                        __slots__ = ["field1", "title", "editor"]
                                        FIELD1_FIELD_NUMBER: ClassVar[int]
                                        TITLE_FIELD_NUMBER: ClassVar[int]
                                        EDITOR_FIELD_NUMBER: ClassVar[int]
                                        field1: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details.field1_type"
                                        title: str
                                        editor: str
                                        
                                        class field1_type(_message.Message):
                                            __slots__ = ["app_id", "package_name"]
                                            APP_ID_FIELD_NUMBER: ClassVar[int]
                                            PACKAGE_NAME_FIELD_NUMBER: ClassVar[int]
                                            app_id: str
                                            package_name: str
                                            def __init__(self, app_id: Optional[str] = ..., package_name: Optional[str] = ...) -> None: ...
                                        
                                        def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details.field1_type"] = ..., title: Optional[str] = ..., editor: Optional[str] = ...) -> None: ...
                                    
                                    def __init__(self, details: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details"] = ...) -> None: ...
                                
                                def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type"] = ...) -> None: ...
                            
                            def __init__(self, icon: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.Icon"] = ..., field6: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type"] = ...) -> None: ...
                        
                        class field234686954_type(_message.Message):
                            __slots__ = ["field1"]
                            FIELD1_FIELD_NUMBER: ClassVar[int]
                            field1: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type"
                            
                            class field1_type(_message.Message):
                                __slots__ = ["field1", "field2"]
                                FIELD1_FIELD_NUMBER: ClassVar[int]
                                FIELD2_FIELD_NUMBER: ClassVar[int]
                                field1: str
                                field2: "GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type.field2_type"
                                
                                class field2_type(_message.Message):
                                    __slots__ = ["field2"]
                                    FIELD2_FIELD_NUMBER: ClassVar[int]
                                    field2: int
                                    def __init__(self, field2: Optional[int] = ...) -> None: ...
                                
                                def __init__(self, field1: Optional[str] = ..., field2: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type.field2_type"] = ...) -> None: ...
                            
                            def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type"] = ...) -> None: ...
                        
                        def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type"] = ..., game: Optional[list["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game"]] = ..., field234686954: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type"] = ...) -> None: ...
                    
                    def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type"] = ...) -> None: ...
                
                class Achievements(_message.Message):
                    __slots__ = ["field1"]
                    FIELD1_FIELD_NUMBER: ClassVar[int]
                    field1: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type"
                    
                    class field1_type(_message.Message):
                        __slots__ = ["field3", "field4"]
                        FIELD3_FIELD_NUMBER: ClassVar[int]
                        FIELD4_FIELD_NUMBER: ClassVar[int]
                        field3: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type"
                        field4: int
                        
                        class field3_type(_message.Message):
                            __slots__ = ["field1", "field2"]
                            FIELD1_FIELD_NUMBER: ClassVar[int]
                            FIELD2_FIELD_NUMBER: ClassVar[int]
                            field1: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type"
                            field2: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type"
                            
                            class field1_type(_message.Message):
                                __slots__ = ["achievement"]
                                ACHIEVEMENT_FIELD_NUMBER: ClassVar[int]
                                achievement: list["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement"]
                                
                                class Achievement(_message.Message):
                                    __slots__ = ["field7"]
                                    FIELD7_FIELD_NUMBER: ClassVar[int]
                                    field7: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type"
                                    
                                    class field7_type(_message.Message):
                                        __slots__ = ["field1"]
                                        FIELD1_FIELD_NUMBER: ClassVar[int]
                                        field1: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type"
                                        
                                        class field1_type(_message.Message):
                                            __slots__ = ["details"]
                                            DETAILS_FIELD_NUMBER: ClassVar[int]
                                            details: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type.Details"
                                            
                                            class Details(_message.Message):
                                                __slots__ = ["title", "description", "xp", "id", "icon_url", "game_id", "timestamp", "field8", "is_secret"]
                                                TITLE_FIELD_NUMBER: ClassVar[int]
                                                DESCRIPTION_FIELD_NUMBER: ClassVar[int]
                                                XP_FIELD_NUMBER: ClassVar[int]
                                                ID_FIELD_NUMBER: ClassVar[int]
                                                ICON_URL_FIELD_NUMBER: ClassVar[int]
                                                GAME_ID_FIELD_NUMBER: ClassVar[int]
                                                TIMESTAMP_FIELD_NUMBER: ClassVar[int]
                                                FIELD8_FIELD_NUMBER: ClassVar[int]
                                                IS_SECRET_FIELD_NUMBER: ClassVar[int]
                                                title: str
                                                description: str
                                                xp: int
                                                id: int
                                                icon_url: str
                                                game_id: str
                                                timestamp: int
                                                field8: int
                                                is_secret: int
                                                def __init__(self, title: Optional[str] = ..., description: Optional[str] = ..., xp: Optional[int] = ..., id: Optional[int] = ..., icon_url: Optional[str] = ..., game_id: Optional[str] = ..., timestamp: Optional[int] = ..., field8: Optional[int] = ..., is_secret: Optional[int] = ...) -> None: ...
                                            
                                            def __init__(self, details: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type.Details"] = ...) -> None: ...
                                        
                                        def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type"] = ...) -> None: ...
                                    
                                    def __init__(self, field7: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type"] = ...) -> None: ...
                                
                                def __init__(self, achievement: Optional[list["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement"]] = ...) -> None: ...
                            
                            class field2_type(_message.Message):
                                __slots__ = ["field1"]
                                FIELD1_FIELD_NUMBER: ClassVar[int]
                                field1: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type"
                                
                                class field1_type(_message.Message):
                                    __slots__ = ["page"]
                                    PAGE_FIELD_NUMBER: ClassVar[int]
                                    page: "GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type.Page"
                                    
                                    class Page(_message.Message):
                                        __slots__ = ["player_id", "next_page_token"]
                                        PLAYER_ID_FIELD_NUMBER: ClassVar[int]
                                        NEXT_PAGE_TOKEN_FIELD_NUMBER: ClassVar[int]
                                        player_id: str
                                        next_page_token: str
                                        def __init__(self, player_id: Optional[str] = ..., next_page_token: Optional[str] = ...) -> None: ...
                                    
                                    def __init__(self, page: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type.Page"] = ...) -> None: ...
                                
                                def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type"] = ...) -> None: ...
                            
                            def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type"] = ..., field2: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type"] = ...) -> None: ...
                        
                        def __init__(self, field3: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type"] = ..., field4: Optional[int] = ...) -> None: ...
                    
                    def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type"] = ...) -> None: ...
                
                def __init__(self, counter: Optional["GetPlayerResponseProto.field1_type.Results.Section.Counter"] = ..., field3: Optional["GetPlayerResponseProto.field1_type.Results.Section.field3_type"] = ..., played_games: Optional["GetPlayerResponseProto.field1_type.Results.Section.PlayedGames"] = ..., achievements: Optional["GetPlayerResponseProto.field1_type.Results.Section.Achievements"] = ...) -> None: ...
            
            def __init__(self, player: Optional["GetPlayerResponseProto.field1_type.Results.Player"] = ..., section: Optional[list["GetPlayerResponseProto.field1_type.Results.Section"]] = ...) -> None: ...
        
        def __init__(self, results: Optional["GetPlayerResponseProto.field1_type.Results"] = ...) -> None: ...
    
    def __init__(self, field1: Optional["GetPlayerResponseProto.field1_type"] = ...) -> None: ...