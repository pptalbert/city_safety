"""Plotly chart factories."""

import plotly.graph_objects as go

from config import RADAR_METRICS
from models import AnalysisResult
from utils.display import score_style
from utils.i18n import location_name, metric_label, tr


def create_gauge(result: AnalysisResult, language: str = "zh") -> go.Figure:
    """Build an overall safety index gauge."""

    label, color = score_style(result.overall_score, language)
    figure = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=result.overall_score,
            title={"text": f"{tr('gauge', language)} · {label}"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": color},
                "steps": [
                    {"range": [0, 30], "color": "#fecaca"},
                    {"range": [30, 50], "color": "#fed7aa"},
                    {"range": [50, 70], "color": "#fef08a"},
                    {"range": [70, 90], "color": "#d9f99d"},
                    {"range": [90, 100], "color": "#bbf7d0"},
                ],
            },
        )
    )
    figure.update_layout(height=360, margin=dict(l=30, r=30, t=70, b=20))
    return figure


def create_radar(result: AnalysisResult, language: str = "zh") -> go.Figure:
    """Build a radar chart from available core metrics."""

    indexed = {metric.key: metric for metric in result.metrics}
    metrics = [indexed[key] for key in RADAR_METRICS if key in indexed]
    labels = [metric_label(metric.key, language) for metric in metrics]
    scores = [metric.score for metric in metrics]
    figure = go.Figure(
        go.Scatterpolar(
            r=scores,
            theta=labels,
            fill="toself",
            name=location_name(result.city.code, language),
        )
    )
    figure.update_layout(
        polar={"radialaxis": {"visible": True, "range": [0, 100]}},
        showlegend=False,
        height=420,
        margin=dict(l=50, r=50, t=40, b=40),
    )
    return figure
