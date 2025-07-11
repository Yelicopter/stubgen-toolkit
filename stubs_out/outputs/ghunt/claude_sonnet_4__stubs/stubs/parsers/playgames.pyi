from typing import *
from datetime import datetime as datetime
from ghunt.objects.apis import Parser

class PlayerProfile(Parser):
    def __init__(self) -> None: ...
    display_name: str
    id: str
    avatar_url: str
    banner_url_portrait: str
    banner_url_landscape: str
    gamertag: str
    last_played_app: PlayerPlayedApp
    profile_settings: PlayerProfileSettings
    experience_info: PlayerExperienceInfo
    title: str

class PlayerPlayedApp(Parser):
    def __init__(self) -> None: ...
    app_id: str
    icon_url: str
    featured_image_url: str
    app_name: str
    timestamp_millis: str

class PlayerExperienceInfo(Parser):
    def __init__(self) -> None: ...
    current_xp: str
    last_level_up_timestamp_millis: str
    current_level: PlayerLevel
    next_level: PlayerLevel
    total_unlocked_achievements: int

class PlayerLevel(Parser):
    def __init__(self) -> None: ...
    level: int
    min_xp: str
    max_xp: str

class PlayerProfileSettings(Parser):
    def __init__(self) -> None: ...
    profile_visible: bool

class PlayedGames(Parser):
    def __init__(self) -> None: ...
    games: List['PlayGame']

class PlayGame(Parser):
    def __init__(self) -> None: ...
    game_data: PlayGameData
    market_data: PlayGameMarketData
    formatted_last_played_time: str
    last_played_time_millis: str
    unlocked_achievement_count: int

class PlayGameMarketData(Parser):
    def __init__(self) -> None: ...
    instances: List['PlayGameMarketInstance']

class PlayGameMarketInstance(Parser):
    def __init__(self) -> None: ...
    id: str
    title: str
    description: str
    images: List['PlayGameImageAsset']
    developer_name: str
    categories: List[str]
    formatted_price: str
    price_micros: str
    badges: List['PlayGameMarketBadge']
    is_owned: bool
    enabled_features: List[str]
    description_snippet: str
    rating: PlayGameMarketRating
    last_updated_timestamp_millis: str
    availability: str

class PlayGameMarketRating(Parser):
    def __init__(self) -> None: ...
    star_rating: float
    ratings_count: str

class PlayGameMarketBadge(Parser):
    def __init__(self) -> None: ...
    badge_type: str
    title: str
    description: str
    images: List['PlayGameImageAsset']

class PlayGameData(Parser):
    def __init__(self) -> None: ...
    id: str
    name: str
    author: str
    description: str
    category: PlayGameCategory
    assets: List['PlayGameImageAsset']
    instances: List['PlayGameInstance']
    last_updated_timestamp: str
    achievement_count: Tuple[int]
    leaderboard_count: Tuple[int]
    enabled_features: List[str]
    theme_color: str

class PlayGameInstance(Parser):
    def __init__(self) -> None: ...
    platform_type: str
    name: str
    turn_based_play: bool
    realtime_play: bool
    android_instance: List['PlayGameAndroidInstance']
    acquisition_uri: str

class PlayGameAndroidInstance(Parser):
    def __init__(self) -> None: ...
    package_name: str
    enable_piracy_check: bool
    preferred: bool

class PlayGameImageAsset(Parser):
    def __init__(self) -> None: ...
    name: str
    width: str
    height: str
    url: str

class PlayGameCategory(Parser):
    def __init__(self) -> None: ...
    primary: str

class PlayerAchievements(Parser):
    def __init__(self) -> None: ...
    achievements: List['PlayerAchievement']

class PlayerAchievement(Parser):
    def __init__(self) -> None: ...
    id: str
    achievement_state: str
    last_updated_timestamp: int
    app_id: int
    xp: str
    definition: PlayerAchievementDefinition

class PlayerAchievementDefinition(Parser):
    def __init__(self) -> None: ...
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

class Player(Parser):
    def __init__(self, profile: PlayerProfile = ..., played_games: List[PlayGame] = ..., achievements: List[PlayerAchievement] = ...) -> None: ...
    profile: PlayerProfile
    played_games: List[PlayGame]
    achievements: List[PlayerAchievement]
