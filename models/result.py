"""Analysis result models."""

from dataclasses import dataclass

from .city import City


@dataclass(frozen=True)
class MetricResult:
    """Hold raw and normalized values for one selected metric."""

    key: str
    label: str
    raw_value: float
    unit: str
    score: float
    weight: int


@dataclass(frozen=True)
class AnalysisResult:
    """Hold the complete result of a city safety analysis."""

    city: City
    overall_score: float
    metrics: tuple[MetricResult, ...]
    environmental_score: float | None = None
    report: str = ""
