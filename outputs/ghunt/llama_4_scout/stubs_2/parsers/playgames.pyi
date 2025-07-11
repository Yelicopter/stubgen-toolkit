from typing import Dict, List
from datetime import datetime

class PlayerProfile:
    def __init__(self) -> None:
        self.display_name: str = ""
        self.id: str = ""
        self.avatar_url: str = ""
        self.banner_url_portrait: str = ""
        self.banner_url_landscape: str = ""
        self.gamertag: str = ""
        self.last_played_app: PlayerPlayedApp = PlayerPlayedApp()
        self.profile_settings: PlayerProfileSettings = PlayerProfileSettings()
        self.experience_info: PlayerExperienceInfo = PlayerExperienceInfo()
        self.title: str = ""

    def _scrape(self, player_data: Dict) -> None:
        ...

class PlayerPlayedApp:
    def __init__(self) -> None:
        self.app_id: str = ""
        self.icon_url: str = ""
        self.featured_image_url: str = ""
        self.app_name: str = ""
        self.timestamp_millis: datetime = datetime.min

    def _scrape(self, played_app_data: Dict) -> None:
        ...

class PlayerExperienceInfo:
    def __init__(self) -> None:
        self.current_xp: str = ""
        self.last_level_up_timestamp_millis: datetime = datetime.min
        self.current_level: PlayerLevel = PlayerLevel()
        self.next_level: PlayerLevel = PlayerLevel()
        self.total_unlocked_achievements: int = 0

    def _scrape(self, experience_data: Dict) -> None:
        ...

class PlayerLevel:
    def __init__(self) -> None:
        self.level: int = 0
        self.min_xp: str = ""
        self.max_xp: str = ""

    def _scrape(self, level_data: Dict) -> None:
        ...

class PlayerProfileSettings:
    def __init__(self) -> None:
        self.profile_visible: bool = False

    def _scrape(self, profile_settings_data: Dict) -> None:
        ...

class PlayedGames:
    def __init__(self) -> None:
        self.games: List[PlayGame] = []

    def _scrape(self, games_data: List[Dict]) -> None:
        ...

class PlayGame:
    def __init__(self) -> None:
        self.game_data: PlayGameData = PlayGameData()
        self.market_data: PlayGameMarketData = PlayGameMarketData()
        self.formatted_last_played_time: str = ""
        self.last_played_time_millis: datetime = datetime.min
        self.unlocked_achievement_count: int = 0

    def _scrape(self, game_data: Dict) -> None:
        ...

class PlayGameMarketData:
    def __init__(self) -> None:
        self.instances: List[PlayGameMarketInstance] = []

    def _scrape(self, market_data: Dict) -> None:
        ...

class PlayGameMarketInstance:
    def __init__(self) -> None:
        self.id: str = ""
        self.title: str = ""
        self.description: str = ""
        self.images: List[PlayGameImageAsset] = []
        self.developer_name: str = ""
        self.categories: List[str] = []
        self.formatted_price: str = ""
        self.price_micros: str = ""
        self.badges: List[PlayGameMarketBadge] = []
        self.is_owned: bool = False
        self.enabled_features: List[str] = []
        self.description_snippet: str = ""
        self.rating: PlayGameMarketRating = PlayGameMarketRating()
        self.last_updated_timestamp_millis: datetime = datetime.min
        self.availability: str = ""

    def _scrape(self, instance_data: Dict) -> None:
        ...

class PlayGameMarketRating:
    def __init__(self) -> None:
        self.star_rating: float = 0.0
        self.ratings_count: str = ""

    def _scrape(self, rating_data: Dict) -> None:
        ...

class PlayGameMarketBadge:
    def __init__(self) -> None:
        self.badge_type: str = ""
        self.title: str = ""
        self.description: str = ""
        self.images: List[PlayGameImageAsset] = []

    def _scrape(self, badge_data: Dict) -> None:
        ...

class PlayGameImageAsset:
    def __init__(self) -> None:
        self.name: str = ""
        self.width: str = ""
        self.height: str = ""
        self.url: str = ""

    def _scrape(self, image_data: Dict) -> None:
        ...

class PlayGameData:
    def __init__(self) -> None:
        self.id: str = ""
        self.name: str = ""
        self.author: str = ""
        self.description: str = ""
        self.category: PlayGameCategory = PlayGameCategory()
        self.assets: List[PlayGameImageAsset] = []
        self.instances: List[PlayGameInstance] = []
        self.last_updated_timestamp: datetime = datetime.min
        self.achievement_count: int = 0
        self.leaderboard_count: int = 0
        self.enabled_features: List[str] = []
        self.theme_color: str = ""

    def _scrape(self, game_data: Dict) -> None:
        ...

class PlayGameInstance:
    def __init__(self) -> None:
        self.platform_type: str = ""
        self.name: str = ""
        self.turn_based_play: bool = False
        self.realtime_play: bool = False
        self.android_instance: List[Dict] = []
        self.acquisition_uri: str = ""

    def _scrape(self, instance_data: Dict) -> None:
        ...

class PlayGameAndroidInstance:
    def __init__(self) -> None:
        self.package_name: str = ""
        self.enable_piracy_check: bool = False
        self.preferred: bool = False

    def _scrape(self, android_instance_data: Dict) -> None:
        ...

class PlayGameCategory:
    def __init__(self) -> None:
        self.primary: str = ""

    def _scrape(self, category_data: Dict) -> None:
        ...

class PlayerAchievements:
    def __init__(self) -> None:
        self.achievements: List[PlayerAchievement] = []

    def _scrape(self, achievements_data: Dict) -> None:
        ...

class PlayerAchievement:
    def __init__(self) -> None:
        self.id: str = ""
        self.achievement_state: str = ""
        self.last_updated_timestamp: datetime = datetime.min
        self.app_id: int = 0
        self.xp: str = ""
        self.definition: PlayerAchievementDefinition = PlayerAchievementDefinition()

    def _scrape(self, achievement_item_data: Dict) -> None:
        ...

class PlayerAchievementDefinition:
    def __init__(self) -> None:
        self.id: str = ""
        self.name: str = ""
        self.description: str = ""
        self.achievement_type: str = ""
        self.xp: str = ""
        self.revealed_icon_url: str = ""
        self.unlocked_icon_url: str = ""
        self.initial_state: str = ""
        self.is_revealed_icon_url_default: bool = False
        self.is_unlocked_icon_url_default: bool = False
        self.rarity_percent: float = 0.0

    def _scrape(self, achievement_def_data: Dict) -> None:
        ...

class Player:
    def __init__(self, profile: PlayerProfile = PlayerProfile(),
                played_games: List[PlayGame] = [],
                achievements: List[PlayerAchievement] = []):
        self.profile: PlayerProfile = profile
        self.played_games: List[PlayGame] = played_games
        self.achievements: List[PlayerAchievement] = achievements