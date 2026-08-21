"""Safety index calculation service."""

from config import METRICS
from models import AnalysisResult, City, MetricResult


class SafetyIndexCalculator:
    """Normalize raw metrics and calculate a weighted safety index."""

    @staticmethod
    def normalize(metric_key: str, raw_value: float) -> float:
        """Convert a raw value to a 0–100 score where higher is safer."""

        config = METRICS[metric_key]
        bounded = min(max(raw_value, config.minimum), config.maximum)
        ratio = (bounded - config.minimum) / (config.maximum - config.minimum)
        score = ratio * 100 if config.higher_is_safer else (1 - ratio) * 100
        return round(score, 1)

    def calculate(
        self,
        city: City,
        raw_values: dict[str, float],
        weights: dict[str, int],
    ) -> AnalysisResult:
        """Calculate metric scores and their weighted overall score."""

        if not raw_values:
            raise ValueError("至少需要选择一个指标。")
        total_weight = sum(
            weights.get(key, 0)
            for key in raw_values
            if METRICS[key].contributes_to_overall
        )
        if total_weight <= 0:
            raise ValueError("所选指标的总权重必须大于 0。")

        scores = {
            key: self.normalize(key, value) for key, value in raw_values.items()
        }
        results = tuple(
            MetricResult(
                key=key,
                label=METRICS[key].label,
                raw_value=value,
                unit=METRICS[key].unit,
                score=scores[key],
                weight=(
                    weights.get(key, 0)
                    if (
                        METRICS[key].contributes_to_overall
                        or METRICS[key].contributes_to_environment
                    )
                    else 0
                ),
            )
            for key, value in raw_values.items()
        )
        overall = sum(
            item.score * item.weight
            for item in results
            if METRICS[item.key].contributes_to_overall
        ) / total_weight
        environmental_weight = sum(
            item.weight
            for item in results
            if METRICS[item.key].contributes_to_environment
        )
        environmental_score = (
            sum(
                item.score * item.weight
                for item in results
                if METRICS[item.key].contributes_to_environment
            ) / environmental_weight
            if environmental_weight > 0
            else None
        )
        return AnalysisResult(
            city=city,
            overall_score=round(overall, 1),
            metrics=results,
            environmental_score=(
                round(environmental_score, 1)
                if environmental_score is not None
                else None
            ),
        )
