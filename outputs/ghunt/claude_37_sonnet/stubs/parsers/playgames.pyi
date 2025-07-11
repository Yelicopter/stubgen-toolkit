from typing import *
from datetime import datetime
from ghunt.objects.apis import Parser

class PlayerProfile(Parser):
    display_name: str
    id: str
    avatar_url: str
    banner_url_portrait: str
    banner_url_landscape: str
    gamertag: str
    last_played_app: 'PlayerPlayedApp'
    profile_settings: 'PlayerProfileSettings'
    experience_info: 'PlayerExperienceInfo'
    title: str
    
    def __init__(self) -> None: ...
    def _scrape(self, player_data: Dict[str, Any]) -> None: ...

class PlayerPlayedApp(Parser):
    app_id: str
    icon_url: str
    featured_image_url: str
    app_name: str
    timestamp_millis: Union[str, datetime]
    
    def __init__(self) -> None: ...
    def _scrape(self, played_app_data: Dict[str, Any]) -> None: ...

class PlayerExperienceInfo(Parser):
    current_xp: str
    last_level_up_timestamp_millis: Union[str, datetime]
    current_level: 'PlayerLevel'
    next_level: 'PlayerLevel'
    total_unlocked_achievements: int
    
    def __init__(self) -> None: ...
    def _scrape(self, experience_data: Dict[str, Any]) -> None: ...

class PlayerLevel(Parser):
    level: int
    min_xp: str
    max_xp: str
    
    def __init__(self) -> None: ...
    def _scrape(self, level_data: Dict[str, Any]) -> None: ...

class PlayerProfileSettings(Parser):
    profile_visible: bool
    
    def __init__(self) -> None: ...
    def _scrape(self, profile_settings_data: Dict[str, Any]) -> None: ...

class PlayedGames(Parser):
    games: List['PlayGame']
    
    def __init__(self) -> None: ...
    def _scrape(self, games_data: List[Dict[str, Any]]) -> None: ...

class PlayGame(Parser):
    game_data: 'PlayGameData'
    market_data: 'PlayGameMarketData'
    formatted_last_played_time: str
    last_played_time_millis: Union[str, datetime]
    unlocked_achievement_count: int
    
    def __init__(self) -> None: ...
    def _scrape(self, game_data: Dict[str, Any]) -> None: ...

class PlayGameMarketData(Parser):
    instances: List['PlayGameMarketInstance']
    
    def __init__(self) -> None: ...
    def _scrape(self, market_data: Dict[str, Any]) -> None: ...

class PlayGameMarketInstance(Parser):
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
    rating: 'PlayGameMarketRating'
    last_updated_timestamp_millis: Union[str, datetime]
    availability: str
    
    def __init__(self) -> None: ...
    def _scrape(self, instance_data: Dict[str, Any]) -> None: ...

class PlayGameMarketRating(Parser):
    star_rating: float
    ratings_count: str
    
    def __init__(self) -> None: ...
    def _scrape(self, rating_data: Dict[str, Any]) -> None: ...

class PlayGameMarketBadge(Parser):
    badge_type: str
    title: str
    description: str
    images: List['PlayGameImageAsset']
    
    def __init__(self) -> None: ...
    def _scrape(self, badge_data: Dict[str, Any]) -> None: ...

class PlayGameData(Parser):
    id: str
    name: str
    author: str
    description: str
    category: 'PlayGameCategory'
    assets: List['PlayGameImageAsset']
    instances: List['PlayGameInstance']
    last_updated_timestamp: Union[str, datetime]
    achievement_count: Tuple[int, ...]
    leaderboard_count: Tuple[int, ...]
    enabled_features: List[str]
    theme_color: str
    
    def __init__(self) -> None: ...
    def _scrape(self, game_data: Dict[str, Any]) -> None: ...

class PlayGameInstance(Parser):
    platform_type: str
    name: str
    turn_based_play: bool
    realtime_play: bool
    android_instance: List['PlayGameAndroidInstance']
    acquisition_uri: str
    
    def __init__(self) -> None: ...
    def _scrape(self, instance_data: Dict[str, Any]) -> None: ...

class PlayGameAndroidInstance(Parser):
    package_name: str
    enable_piracy_check: bool
    preferred: bool
    
    def __init__(self) -> None: ...
    def _scrape(self, android_instance_data: Dict[str, Any]) -> None: ...

class PlayGameImageAsset(Parser):
    name: str
    width: str
    height: str
    url: str
    
    def __init__(self) -> None: ...
    def _scrape(self, image_data: Dict[str, Any]) -> None: ...

class PlayGameCategory(Parser):
    primary: str
    
    def __init__(self) -> None: ...
    def _scrape(self, category_data: Dict[str, Any]) -> None: ...

class PlayerAchievements(Parser):
    achievements: List['PlayerAchievement']
    
    def __init__(self) -> None: ...
    def _scrape(self, achievements_data: Dict[str, Any]) -> None: ...

class PlayerAchievement(Parser):
    id: str
    achievement_state: str
    last_updated_timestamp: int
    app_id: int
    xp: str
    definition: 'PlayerAchievementDefinition'
    
    def __init__(self) -> None: ...
    def _scrape(self, achievement_item_data: Dict[str, Any]) -> None: ...

class PlayerAchievementDefinition(Parser):
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
    def _scrape(self, achievement_def_data: Dict[str, Any]) -> None: ...

class Player(Parser):
    profile: PlayerProfile
    played_games: List[Any]
    achievements: List[Any]
    
    def __init__(self, profile: PlayerProfile = PlayerProfile(),
                played_games: List[Any] = [],
                achievements: List[Any] = []) -> None: ...