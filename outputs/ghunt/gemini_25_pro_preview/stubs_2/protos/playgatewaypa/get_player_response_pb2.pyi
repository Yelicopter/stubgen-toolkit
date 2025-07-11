from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import well_known_types as _well_known_types

class GetPlayerResponseProto(_message.Message):
    class field1_type(_message.Message):
        class Results(_message.Message):
            class Player(_message.Message):
                class field1_type(_message.Message):
                    name: str
                    def __init__(self, name: str = ...) -> None: ...
                class Avatar(_message.Message):
                    url: str
                    def __init__(self, url: str = ...) -> None: ...
                field1: GetPlayerResponseProto.field1_type.Results.Player.field1_type
                avatar: GetPlayerResponseProto.field1_type.Results.Player.Avatar
                def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Player.field1_type = ..., avatar: GetPlayerResponseProto.field1_type.Results.Player.Avatar = ...) -> None: ...
            class Section(_message.Message):
                class Counter(_message.Message):
                    number: str
                    def __init__(self, number: str = ...) -> None: ...
                class field3_type(_message.Message):
                    section_name: str
                    def __init__(self, section_name: str = ...) -> None: ...
                class PlayedGames(_message.Message):
                    class field1_type(_message.Message):
                        class field1_type(_message.Message):
                            class field203130867_type(_message.Message):
                                field1: str
                                def __init__(self, field1: str = ...) -> None: ...
                            field203130867: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type.field203130867_type
                            def __init__(self, field203130867: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type.field203130867_type = ...) -> None: ...
                        class Game(_message.Message):
                            class Icon(_message.Message):
                                url: str
                                def __init__(self, url: str = ...) -> None: ...
                            class field6_type(_message.Message):
                                class field1_type(_message.Message):
                                    class Details(_message.Message):
                                        class field1_type(_message.Message):
                                            app_id: str
                                            package_name: str
                                            def __init__(self, app_id: str = ..., package_name: str = ...) -> None: ...
                                        field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details.field1_type
                                        title: str
                                        editor: str
                                        def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details.field1_type = ..., title: str = ..., editor: str = ...) -> None: ...
                                    details: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details
                                    def __init__(self, details: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type.Details = ...) -> None: ...
                                field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type
                                def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type.field1_type = ...) -> None: ...
                            icon: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.Icon
                            field6: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type
                            def __init__(self, icon: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.Icon = ..., field6: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game.field6_type = ...) -> None: ...
                        class field234686954_type(_message.Message):
                            class field1_type(_message.Message):
                                class field2_type(_message.Message):
                                    field2: int
                                    def __init__(self, field2: int = ...) -> None: ...
                                field1: str
                                field2: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type.field2_type
                                def __init__(self, field1: str = ..., field2: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type.field2_type = ...) -> None: ...
                            field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type
                            def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type.field1_type = ...) -> None: ...
                        field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type
                        game: _containers.RepeatedCompositeFieldContainer[GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game]
                        field234686954: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type
                        def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field1_type = ..., game: _containers.RepeatedCompositeFieldContainer[GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.Game] = ..., field234686954: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type.field234686954_type = ...) -> None: ...
                    field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type
                    def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames.field1_type = ...) -> None: ...
                class Achievements(_message.Message):
                    class field1_type(_message.Message):
                        class field3_type(_message.Message):
                            class field1_type(_message.Message):
                                class Achievement(_message.Message):
                                    class field7_type(_message.Message):
                                        class field1_type(_message.Message):
                                            class Details(_message.Message):
                                                title: str
                                                description: str
                                                xp: int
                                                id: int
                                                icon_url: str
                                                game_id: str
                                                timestamp: int
                                                field8: int
                                                is_secret: int
                                                def __init__(self, title: str = ..., description: str = ..., xp: int = ..., id: int = ..., icon_url: str = ..., game_id: str = ..., timestamp: int = ..., field8: int = ..., is_secret: int = ...) -> None: ...
                                            details: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type.Details
                                            def __init__(self, details: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type.Details = ...) -> None: ...
                                        field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type
                                        def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type.field1_type = ...) -> None: ...
                                    field7: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type
                                    def __init__(self, field7: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement.field7_type = ...) -> None: ...
                                achievement: _containers.RepeatedCompositeFieldContainer[GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement]
                                def __init__(self, achievement: _containers.RepeatedCompositeFieldContainer[GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type.Achievement] = ...) -> None: ...
                            class field2_type(_message.Message):
                                class field1_type(_message.Message):
                                    class Page(_message.Message):
                                        player_id: str
                                        next_page_token: str
                                        def __init__(self, player_id: str = ..., next_page_token: str = ...) -> None: ...
                                    page: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type.Page
                                    def __init__(self, page: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type.Page = ...) -> None: ...
                                field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type
                                def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type.field1_type = ...) -> None: ...
                            field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type
                            field2: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type
                            def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field1_type = ..., field2: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type.field2_type = ...) -> None: ...
                        field3: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type
                        field4: int
                        def __init__(self, field3: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type.field3_type = ..., field4: int = ...) -> None: ...
                    field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type
                    def __init__(self, field1: GetPlayerResponseProto.field1_type.Results.Section.Achievements.field1_type = ...) -> None: ...
                counter: GetPlayerResponseProto.field1_type.Results.Section.Counter
                field3: GetPlayerResponseProto.field1_type.Results.Section.field3_type
                played_games: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames
                achievements: GetPlayerResponseProto.field1_type.Results.Section.Achievements
                def __init__(self, counter: GetPlayerResponseProto.field1_type.Results.Section.Counter = ..., field3: GetPlayerResponseProto.field1_type.Results.Section.field3_type = ..., played_games: GetPlayerResponseProto.field1_type.Results.Section.PlayedGames = ..., achievements: GetPlayerResponseProto.field1_type.Results.Section.Achievements = ...) -> None: ...
            player: GetPlayerResponseProto.field1_type.Results.Player
            section: _containers.RepeatedCompositeFieldContainer[GetPlayerResponseProto.field1_type.Results.Section]
            def __init__(self, player: GetPlayerResponseProto.field1_type.Results.Player = ..., section: _containers.RepeatedCompositeFieldContainer[GetPlayerResponseProto.field1_type.Results.Section] = ...) -> None: ...
        results: GetPlayerResponseProto.field1_type.Results
        def __init__(self, results: GetPlayerResponseProto.field1_type.Results = ...) -> None: ...
    field1: GetPlayerResponseProto.field1_type
    def __init__(self, field1: GetPlayerResponseProto.field1_type = ...) -> None: ...