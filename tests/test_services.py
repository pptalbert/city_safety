"""Tests for data and reporting services."""

from models import City
from services.calculator import SafetyIndexCalculator
from services.data_provider import MockCityDataProvider, SourcedCityDataProvider
from services.report_generator import ReportGenerator


def test_mock_data_is_reproducible_and_bounded() -> None:
    """Verify that mock API replacements are stable for a city and metric."""

    provider = MockCityDataProvider()
    city = City("加拿大", "多伦多", "CA-TOR")
    first = provider.fetch_metric(city, "safety_crime_rate")
    second = provider.fetch_metric(city, "safety_crime_rate")
    assert first == second
    assert 2 <= first <= 100


def test_mock_purchasing_power_reflects_local_costs() -> None:
    """Verify the demonstration values for China and San Francisco."""

    provider = MockCityDataProvider()
    china = provider.fetch_metric(City("中国", "北京", "CN-BJ"), "purchasing_power_parity")
    san_francisco = provider.fetch_metric(
        City("美国", "旧金山", "US-SFO"), "purchasing_power_parity"
    )
    assert china > san_francisco


def test_toronto_density_uses_official_census_value() -> None:
    """Verify Toronto density and provenance use the 2021 census record."""

    provider = SourcedCityDataProvider()
    city = City("加拿大", "多伦多", "CA-TOR")
    assert provider.fetch_metric(city, "population_density") == 4427.8
    source = provider.source_for(city, "population_density")
    assert source["kind"] == "official"
    assert source["as_of"] == "2021"
    assert "Statistics Canada" in source["source_name"]


def test_unsourced_metric_is_explicitly_marked_mock() -> None:
    """Verify missing observations never masquerade as real data."""

    provider = SourcedCityDataProvider()
    city = City("加拿大", "多伦多", "CA-TOR")
    assert provider.source_for(city, "night_lighting")["kind"] == "mock"


def test_every_selectable_city_has_sourced_population_density() -> None:
    """Verify that population-density coverage spans the entire city catalog."""

    provider = SourcedCityDataProvider()
    city_catalog = (
        ("CN-BJ", "北京"), ("CN-SH", "上海"), ("CN-GZ", "广州"),
        ("CN-SZ", "深圳"), ("CA-TOR", "多伦多"), ("CA-VAN", "温哥华"),
        ("CA-MTL", "蒙特利尔"), ("US-NYC", "纽约"),
        ("US-SFO", "旧金山"), ("US-CHI", "芝加哥"),
        ("GB-LON", "伦敦"), ("FR-PAR", "巴黎"), ("JP-TYO", "东京"),
        ("SG-SIN", "新加坡"), ("AU-SYD", "悉尼"),
    )
    for code, name in city_catalog:
        city = City("", name, code)
        value = provider.fetch_metric(city, "population_density")
        source = provider.source_for(city, "population_density")
        assert value > 0
        assert source["kind"] == "official"
        assert source["as_of"]
        assert source["geography"]
        assert source["source_url"].startswith("https://")


def test_report_mentions_strength_and_weakness() -> None:
    """Verify that generated reports explain both sides of the result."""

    city = City("测试国", "测试市", "TEST")
    result = SafetyIndexCalculator().calculate(
        city,
        {"night_lighting": 10, "education_level": 90},
        {"night_lighting": 50, "education_level": 50},
    )
    report = ReportGenerator.generate(result)
    assert "教育水平" in report
    assert "夜间照明" in report
    assert "夜间" in report


def test_report_can_be_generated_in_all_languages() -> None:
    """Verify that every supported language produces a localized report."""

    city = City("加拿大", "多伦多", "CA-TOR")
    result = SafetyIndexCalculator().calculate(
        city,
        {"night_lighting": 10, "education_level": 90},
        {"night_lighting": 50, "education_level": 50},
    )
    reports = {
        language: ReportGenerator.generate(result, language)
        for language in ("zh", "en", "ja", "fr", "es", "de")
    }
    assert len(set(reports.values())) == 6
    assert "Toronto" in reports["en"]
    assert "éclairage" in reports["fr"].lower()


def test_report_generator_accepts_language_as_positional_argument() -> None:
    """Regress the Streamlit call form that previously raised TypeError."""

    city = City("加拿大", "多伦多", "CA-TOR")
    result = SafetyIndexCalculator().calculate(
        city, {"night_lighting": 50}, {"night_lighting": 100}
    )
    assert "Toronto" in ReportGenerator.generate(result, "en")


def test_report_has_separate_weighted_environment_topic() -> None:
    result = SafetyIndexCalculator().calculate(
        City("加拿大", "多伦多", "CA-TOR"),
        {"night_lighting": 80, "air_quality": 20, "green_space": 90},
        {"night_lighting": 100, "air_quality": 75, "green_space": 25},
    )
    report = ReportGenerator.generate(result, "en")
    assert "environmental score is 37.5/100" in report
    assert "Air quality" in report
    assert "not the overall safety index" in report
