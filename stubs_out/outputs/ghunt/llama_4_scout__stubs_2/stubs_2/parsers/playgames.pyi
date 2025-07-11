from _typeshed import Incomplete
from typing import List

class PlayerProfile:
    display_name: str
    id: str
    avatar_url: str
    banner_url_portrait: str
    banner_url_landscape: str
    gamertag: str
    last_played_app: Incomplete
    profile_settings: Incomplete
    experience_info: Incomplete
    title: str
    def __init__(self) -> None: ...

class PlayerPlayedApp:
    app_id: str
    icon_url: str
    featured_image_url: str
    app_name: str
    timestamp_millis: Incomplete
    def __init__(self) -> None: ...

class PlayerExperienceInfo:
    current_xp: str
    last_level_up_timestamp_millis: Incomplete
    current_level: Incomplete
    next_level: Incomplete
    total_unlocked_achievements: int
    def __init__(self) -> None: ...

class PlayerLevel:
    level: int
    min_xp: str
    max_xp: str
    def __init__(self) -> None: ...

class PlayerProfileSettings:
    profile_visible: bool
    def __init__(self) -> None: ...

class PlayedGames:
    games: Incomplete
    def __init__(self) -> None: ...

class PlayGame:
    game_data: Incomplete
    market_data: Incomplete
    formatted_last_played_time: str
    last_played_time_millis: Incomplete
    unlocked_achievement_count: int
    def __init__(self) -> None: ...

class PlayGameMarketData:
    instances: Incomplete
    def __init__(self) -> None: ...

class PlayGameMarketInstance:
    id: str
    title: str
    description: str
    images: Incomplete
    developer_name: str
    categories: Incomplete
    formatted_price: str
    price_micros: str
    badges: Incomplete
    is_owned: bool
    enabled_features: Incomplete
    description_snippet: str
    rating: Incomplete
    last_updated_timestamp_millis: Incomplete
    availability: str
    def __init__(self) -> None: ...

class PlayGameMarketRating:
    star_rating: float
    ratings_count: str
    def __init__(self) -> None: ...

class PlayGameMarketBadge:
    badge_type: str
    title: str
    description: str
    images: Incomplete
    def __init__(self) -> None: ...

class PlayGameImageAsset:
    name: str
    width: str
    height: str
    url: str
    def __init__(self) -> None: ...

class PlayGameData:
    id: str
    name: str
    author: str
    description: str
    category: Incomplete
    assets: Incomplete
    instances: Incomplete
    last_updated_timestamp: Incomplete
    achievement_count: int
    leaderboard_count: int
    enabled_features: Incomplete
    theme_color: str
    def __init__(self) -> None: ...

class PlayGameInstance:
    platform_type: str
    name: str
    turn_based_play: bool
    realtime_play: bool
    android_instance: Incomplete
    acquisition_uri: str
    def __init__(self) -> None: ...

class PlayGameAndroidInstance:
    package_name: str
    enable_piracy_check: bool
    preferred: bool
    def __init__(self) -> None: ...

class PlayGameCategory:
    primary: str
    def __init__(self) -> None: ...

class PlayerAchievements:
    achievements: Incomplete
    def __init__(self) -> None: ...

class PlayerAchievement:
    id: str
    achievement_state: str
    last_updated_timestamp: Incomplete
    app_id: int
    xp: str
    definition: Incomplete
    def __init__(self) -> None: ...

class PlayerAchievementDefinition:
    id: str
    name: str
    description: str
    achievement_type: str
    xp: str
    revealed_icon_url: str
    unlocked_icon_url: str
    initial_state: str
    is_revealed_icon_url_default: bool
    is_unlocked_icon_url_default: bool
    rarity_percent: float
    def __init__(self) -> None: ...

class Player:
    profile: Incomplete
    played_games: Incomplete
    achievements: Incomplete
    def __init__(self, profile: PlayerProfile = ..., played_games: List[PlayGame] = ..., achievements: List[PlayerAchievement] = ...) -> None: ...
