"""Display classifications for safety scores."""


from utils.i18n import level_label


def score_style(score: float, language: str = "zh") -> tuple[str, str]:
    """Return the localized classification and color for a score."""

    if score >= 90:
        return level_label("very_safe", language), "#15803d"
    if score >= 70:
        return level_label("safe", language), "#65a30d"
    if score >= 50:
        return level_label("moderate", language), "#eab308"
    if score >= 30:
        return level_label("high_risk", language), "#f97316"
    return level_label("dangerous", language), "#dc2626"
