"""Streamlit entry point for City Safety Index."""

from dataclasses import replace
import importlib
from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import config as config_module
import models as models_module
from models import result as result_model_module
from services import calculator as calculator_module
from services import data_provider as data_provider_module
from services import report_generator as report_module
from utils import charts as charts_module
from utils import display as display_module
from utils import i18n as i18n_module

# Streamlit reruns the entry script in the same Python process. Reload the full
# local dependency chain in order so new metric schemas are never combined
# with cached services or presentation functions from an earlier revision.
for local_module in (
    config_module,
    result_model_module,
    models_module,
    calculator_module,
    data_provider_module,
    i18n_module,
    display_module,
    charts_module,
    report_module,
):
    importlib.reload(local_module)

APP_TITLE = config_module.APP_TITLE
DEFAULT_WEIGHT = config_module.DEFAULT_WEIGHT
METRICS = config_module.METRICS
METRIC_SCHEMA_VERSION = config_module.METRIC_SCHEMA_VERSION
AnalysisResult = models_module.AnalysisResult
City = models_module.City
SafetyIndexCalculator = calculator_module.SafetyIndexCalculator
MockCityDataProvider = data_provider_module.MockCityDataProvider
SourcedCityDataProvider = data_provider_module.SourcedCityDataProvider
ReportGenerator = report_module.ReportGenerator
create_gauge = charts_module.create_gauge
create_radar = charts_module.create_radar
score_style = display_module.score_style
LANGUAGES = i18n_module.LANGUAGES
location_name = i18n_module.location_name
location_part = i18n_module.location_part
metric_help = i18n_module.metric_help
metric_label = i18n_module.metric_label
metric_unit = i18n_module.metric_unit
tr = i18n_module.tr


@st.cache_data
def load_cities() -> pd.DataFrame:
    """Load the bundled searchable city catalog."""

    path = Path(__file__).parent / "data" / "cities.csv"
    return pd.read_csv(path)


def render_metric_card(
    key: str,
    score: float,
    raw: float,
    language: str,
    source: dict[str, str] | None = None,
) -> None:
    """Render one color-coded metric summary card."""

    status, color = score_style(score, language)
    label = metric_label(key, language)
    details = tr(
        "environment_score_raw" if METRICS[key].contributes_to_environment else "score_raw",
        language, score=f"{score:.1f}", raw=f"{raw:,.2f}",
        unit=metric_unit(key, language),
    )
    st.markdown(
        f"""
        <div style="border-left:6px solid {color};padding:10px 14px;
                    margin:7px 0;background:#f8fafc;border-radius:6px">
          <strong>{label}</strong> · {status}<br>
          {details}
        </div>
        """,
        unsafe_allow_html=True,
    )
    if source and source.get("kind") == "official":
        st.caption(
            tr(
                "official_source",
                language,
                year=source.get("as_of", ""),
                geography=source.get("geography", ""),
            )
        )
        st.markdown(f"[{source['source_name']}]({source['source_url']})")
    else:
        st.caption(tr("mock_source", language))


def generate_report(result: AnalysisResult, language: str) -> str:
    """Generate a report while tolerating a stale pre-localization module.

    Streamlit may keep imported service modules in memory while reloading the
    entry script. The fallback prevents an active development session from
    crashing once; a clean rerun then uses the localized signature.
    """

    try:
        return ReportGenerator.generate(result, language)
    except TypeError as error:
        if "positional argument" not in str(error):
            raise
        return ReportGenerator.generate(result)


def generate_chart(
    factory: object, result: AnalysisResult, language: str
) -> go.Figure:
    """Build a localized chart while tolerating a stale chart module.

    During Streamlit hot reloads, ``app.py`` can briefly coexist with an older
    cached version of ``utils.charts`` whose factories only accept one argument.
    """

    try:
        return factory(result, language)  # type: ignore[operator]
    except TypeError as error:
        if "positional argument" not in str(error):
            raise
        return factory(result)  # type: ignore[operator]


def main() -> None:
    """Render the application and execute analyses on demand."""

    st.set_page_config(page_title=APP_TITLE, page_icon="🏙️", layout="wide")
    if st.session_state.get("metric_schema_version") != METRIC_SCHEMA_VERSION:
        st.session_state.pop("analysis_result", None)
        st.session_state.pop("metric_sources", None)
        st.session_state["metric_schema_version"] = METRIC_SCHEMA_VERSION
    st.title("🏙️ City Safety Index")
    language = st.selectbox(
        "Language / 语言", list(LANGUAGES), format_func=LANGUAGES.get,
        key="language",
    )
    st.caption(tr("caption", language))

    cities = load_cities()
    countries = sorted(cities["country"].unique())
    left, right = st.columns(2)
    country = left.selectbox(
        tr("country", language), countries,
        format_func=lambda value: location_part(
            str(cities[cities["country"] == value].iloc[0]["code"]), language, 0
        ),
    )
    city_rows = cities[cities["country"] == country]
    city_code = right.selectbox(
        tr("city", language), sorted(city_rows["code"].astype(str).tolist()),
        format_func=lambda code: location_part(code, language, 1),
    )
    row = city_rows[city_rows["code"] == city_code].iloc[0]
    city_name = str(row["city"])
    city = City(country=country, name=city_name, code=str(row["code"]))

    st.subheader(tr("factors", language))
    selected: list[str] = []
    weights: dict[str, int] = {}
    columns = st.columns(2)
    for index, (key, metric) in enumerate(METRICS.items()):
        with columns[index % 2]:
            enabled = st.checkbox(metric_label(key, language), value=key in {
                "safety_crime_rate", "purchasing_power_parity", "education_level",
                "population_density", "public_transport", "police_count",
            }, key=f"enabled_{key}", help=metric_help(key, language))
            if enabled:
                selected.append(key)
                if metric.contributes_to_overall or metric.contributes_to_environment:
                    weights[key] = st.slider(
                        tr("weight", language, name=metric_label(key, language)),
                        0, 100, DEFAULT_WEIGHT, key=f"weight_{key}",
                        help=f"{metric_help(key, language)}\n\n{tr('environment_weight_help' if metric.contributes_to_environment else 'weight_help', language)}",
                    )
                    if metric.contributes_to_environment:
                        st.caption(tr("environmental_factor_role", language))
                else:
                    weights[key] = 0
                    st.caption(tr(f"{key}_role", language))

    if st.button(tr("analyze", language), type="primary", use_container_width=True):
        if not selected:
            st.error(tr("select_error", language))
            return
        safety_weight = sum(
            weights.get(key, 0)
            for key in selected
            if METRICS[key].contributes_to_overall
        )
        if safety_weight == 0:
            st.error(tr("weight_error", language))
            return

        with st.spinner(tr("loading", language)):
            provider = SourcedCityDataProvider()
            raw_values = provider.fetch_metrics(city, selected)
            st.session_state["metric_sources"] = {
                key: dict(provider.source_for(city, key)) for key in selected
            }
            result = SafetyIndexCalculator().calculate(city, raw_values, weights)
            result = replace(result, report=generate_report(result, language))
            st.session_state["analysis_result"] = result

    result = st.session_state.get("analysis_result")
    if result is None:
        st.info(tr("prompt", language))
        return

    st.divider()
    place = location_name(result.city.code, language)
    st.header(tr("results", language, place=place))
    gauge_column, radar_column = st.columns(2)
    gauge_column.plotly_chart(
        generate_chart(create_gauge, result, language), width="stretch"
    )
    if len(result.metrics) >= 3:
        radar_column.plotly_chart(
            generate_chart(create_radar, result, language), width="stretch"
        )
    else:
        radar_column.info(tr("radar_hint", language))

    st.subheader(tr("metrics", language))
    metric_sources = st.session_state.get("metric_sources", {})
    for metric in result.metrics:
        render_metric_card(
            metric.key,
            metric.score,
            metric.raw_value,
            language,
            metric_sources.get(metric.key),
        )

    st.subheader(tr("report", language))
    st.success(generate_report(result, language))
    if result.environmental_score is not None:
        st.metric(
            tr("environment_score", language),
            f"{result.environmental_score:.1f}/100",
            help=tr("environment_score_help", language),
        )
    with st.expander(tr("calculation", language)):
        st.write(tr("normalization", language))
        st.write(tr("formula", language))


if __name__ == "__main__":
    main()
