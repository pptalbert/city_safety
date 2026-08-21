"""Application-wide configuration and metric metadata."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MetricConfig:
    """Describe a safety metric and how its raw value is normalized."""

    key: str
    label: str
    unit: str
    minimum: float
    maximum: float
    higher_is_safer: bool
    contributes_to_overall: bool = True
    contributes_to_environment: bool = False


APP_TITLE = "City Safety Index"
DEFAULT_WEIGHT = 50
METRIC_SCHEMA_VERSION = 5

METRICS: dict[str, MetricConfig] = {
    "safety_crime_rate": MetricConfig(
        "safety_crime_rate", "人身与财产安全犯罪率", "每千人案件", 2, 100, False
    ),
    "other_crime_rate": MetricConfig(
        "other_crime_rate", "其他犯罪率", "每千人案件", 1, 80, False, False
    ),
    "unemployment_rate": MetricConfig("unemployment_rate", "失业率", "%", 2, 20, False),
    "purchasing_power_parity": MetricConfig(
        "purchasing_power_parity", "购买力平价", "本地购买力指数", 0, 100, True
    ),
    "population_density": MetricConfig("population_density", "人口密度", "人/km²", 100, 20_000, False),
    "night_lighting": MetricConfig("night_lighting", "夜间照明", "覆盖指数", 0, 100, True),
    "police_count": MetricConfig("police_count", "警察数量", "每万人", 5, 60, True),
    "education_level": MetricConfig("education_level", "教育水平", "综合指数", 0, 100, True),
    "housing_price": MetricConfig("housing_price", "房价", "USD/m²", 500, 20_000, True),
    "tourist_count": MetricConfig("tourist_count", "游客数量", "万人/年", 1, 3_000, True),
    "public_transport": MetricConfig("public_transport", "公共交通便利程度", "综合指数", 0, 100, True),
    "air_quality": MetricConfig(
        "air_quality", "空气质量", "空气质量指数", 0, 100, True, False, True
    ),
    "water_quality": MetricConfig(
        "water_quality", "水质", "水质指数", 0, 100, True, False, True
    ),
    "green_space": MetricConfig(
        "green_space", "绿色空间", "覆盖与可达性指数", 0, 100, True, False, True
    ),
    "noise_environment": MetricConfig(
        "noise_environment", "声环境", "安静程度指数", 0, 100, True, False, True
    ),
    "climate_resilience": MetricConfig(
        "climate_resilience", "气候韧性", "韧性指数", 0, 100, True, False, True
    ),
    "social_media_reputation": MetricConfig(
        "social_media_reputation", "社交媒体口碑", "安全口碑指数", 0, 100, True
    ),
}

RADAR_METRICS = (
    "safety_crime_rate",
    "purchasing_power_parity",
    "education_level",
    "population_density",
    "public_transport",
    "police_count",
)
