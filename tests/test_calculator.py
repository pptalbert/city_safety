"""Tests for safety index calculations."""

import pytest

from models import City
from services.calculator import SafetyIndexCalculator


def test_lower_crime_rate_produces_higher_score() -> None:
    """Verify that a negative metric is normalized in the safe direction."""

    calculator = SafetyIndexCalculator()
    assert calculator.normalize("safety_crime_rate", 2) == 100
    assert calculator.normalize("safety_crime_rate", 100) == 0


def test_weighted_calculation() -> None:
    """Verify that the overall score respects user weights."""

    city = City("测试国", "测试市", "TEST")
    result = SafetyIndexCalculator().calculate(
        city,
        {"night_lighting": 100, "education_level": 0},
        {"night_lighting": 75, "education_level": 25},
    )
    assert result.overall_score == 75.0


def test_zero_total_weight_is_rejected() -> None:
    """Verify that a meaningless all-zero weighting is rejected."""

    with pytest.raises(ValueError, match="总权重"):
        SafetyIndexCalculator().calculate(
            City("测试国", "测试市", "TEST"), {"night_lighting": 50}, {"night_lighting": 0}
        )


def test_environment_is_reported_but_does_not_change_overall_score() -> None:
    """Verify that environmental state remains outside the crime-safety sum."""

    calculator = SafetyIndexCalculator()
    city = City("测试国", "测试市", "TEST")
    baseline = calculator.calculate(
        city, {"night_lighting": 80}, {"night_lighting": 100}
    )
    with_environment = calculator.calculate(
        city,
        {"night_lighting": 80, "air_quality": 0, "green_space": 100},
        {"night_lighting": 100, "air_quality": 75, "green_space": 25},
    )
    assert with_environment.overall_score == baseline.overall_score
    assert next(
        item for item in with_environment.metrics if item.key == "air_quality"
    ).weight == 75
    assert with_environment.environmental_score == 25.0


def test_environmental_weights_change_only_environmental_score() -> None:
    calculator = SafetyIndexCalculator()
    city = City("测试国", "测试市", "TEST")
    air_weighted = calculator.calculate(
        city,
        {"night_lighting": 80, "air_quality": 20, "water_quality": 80},
        {"night_lighting": 100, "air_quality": 100, "water_quality": 0},
    )
    water_weighted = calculator.calculate(
        city,
        {"night_lighting": 80, "air_quality": 20, "water_quality": 80},
        {"night_lighting": 100, "air_quality": 0, "water_quality": 100},
    )
    assert air_weighted.overall_score == water_weighted.overall_score
    assert air_weighted.environmental_score == 20.0
    assert water_weighted.environmental_score == 80.0


def test_purchasing_power_parity_directly_affects_score() -> None:
    """Verify that PPP replaces nominal income as a direct factor."""

    calculator = SafetyIndexCalculator()
    city = City("测试国", "测试市", "TEST")
    low_power = calculator.calculate(city, {"purchasing_power_parity": 25}, {"purchasing_power_parity": 100})
    high_power = calculator.calculate(city, {"purchasing_power_parity": 85}, {"purchasing_power_parity": 100})
    assert high_power.overall_score > low_power.overall_score


def test_other_crime_does_not_change_visitor_safety_score() -> None:
    """Verify that visitor-irrelevant crime is background information only."""

    calculator = SafetyIndexCalculator()
    city = City("测试国", "测试市", "TEST")
    baseline = calculator.calculate(city, {"safety_crime_rate": 20}, {"safety_crime_rate": 100})
    combined = calculator.calculate(
        city,
        {"safety_crime_rate": 20, "other_crime_rate": 80},
        {"safety_crime_rate": 100, "other_crime_rate": 100},
    )
    assert combined.overall_score == baseline.overall_score
    assert next(item for item in combined.metrics if item.key == "other_crime_rate").weight == 0
