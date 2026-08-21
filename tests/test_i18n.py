"""Tests for localization helpers."""

from config import METRICS
from utils.i18n import LANGUAGES, metric_help, metric_label, tr
from models import City
from services.calculator import SafetyIndexCalculator
from utils.charts import create_gauge, create_radar
from utils.display import score_style


def test_every_metric_has_text_and_help_in_every_language() -> None:
    """Verify that factor controls never display missing translations."""

    for language in LANGUAGES:
        for key in METRICS:
            assert metric_label(key, language)
            assert metric_help(key, language)


def test_common_interface_text_is_localized() -> None:
    """Verify that language switching changes common interface labels."""

    labels = {language: tr("analyze", language) for language in LANGUAGES}
    assert len(set(labels.values())) == len(LANGUAGES)


def test_chart_factories_accept_language_as_positional_argument() -> None:
    """Regress the localized chart call form used by the Streamlit app."""

    result = SafetyIndexCalculator().calculate(
        City("加拿大", "多伦多", "CA-TOR"),
        {
            "safety_crime_rate": 30,
            "purchasing_power_parity": 60,
            "education_level": 80,
        },
        {"safety_crime_rate": 50, "purchasing_power_parity": 50, "education_level": 50},
    )
    assert "Overall Safety Index" in create_gauge(result, "en").data[0].title.text
    assert create_radar(result, "fr").data[0].theta[0] == "Criminalité contre les personnes/biens"


def test_score_style_accepts_and_uses_language() -> None:
    """Regress localized safety levels passed as a second argument."""

    assert score_style(95, "en")[0] == "Very safe"
    assert score_style(55, "fr")[0] == "Modéré"
    assert score_style(20, "de")[0] == "Gefährlich"
