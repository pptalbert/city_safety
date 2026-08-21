"""Data provider abstractions and a deterministic mock implementation."""

from abc import ABC, abstractmethod
import csv
import hashlib
from pathlib import Path
import random
from typing import TypedDict

from config import METRICS
from models import City


class SourceInfo(TypedDict):
    """Describe the provenance and scope of one metric value."""

    kind: str
    as_of: str
    geography: str
    source_name: str
    source_url: str


class CityDataProvider(ABC):
    """Define the interface implemented by city data sources."""

    @abstractmethod
    def fetch_metric(self, city: City, metric_key: str) -> float:
        """Return a raw metric value for a city."""

    def fetch_metrics(self, city: City, metric_keys: list[str]) -> dict[str, float]:
        """Return raw values for all requested metrics."""

        return {key: self.fetch_metric(city, key) for key in metric_keys}

    def source_for(self, city: City, metric_key: str) -> SourceInfo:
        """Return provenance information for a city metric."""

        return SourceInfo(
            kind="unknown",
            as_of="",
            geography=city.name,
            source_name="Unknown",
            source_url="",
        )


class MockCityDataProvider(CityDataProvider):
    """Generate stable mock values, suitable for development and demos."""

    def fetch_metric(self, city: City, metric_key: str) -> float:
        """Generate a reproducible value within the metric's configured range."""

        if metric_key == "purchasing_power_parity":
            purchasing_power = {
                "CN": 85,
                "CA": 62,
                "US": 48,
                "GB": 47,
                "FR": 55,
                "JP": 58,
                "SG": 50,
                "AU": 52,
            }.get(city.code[:2], 50)
            # San Francisco is deliberately lower to demonstrate that the
            # same nominal income buys less in a very high-cost city.
            return 25.0 if city.code == "US-SFO" else float(purchasing_power)

        metric = METRICS[metric_key]
        seed_bytes = hashlib.sha256(f"{city.code}:{metric_key}".encode()).digest()
        generator = random.Random(int.from_bytes(seed_bytes[:8], "big"))
        return round(generator.uniform(metric.minimum, metric.maximum), 2)

    def source_for(self, city: City, metric_key: str) -> SourceInfo:
        """Identify values produced by the deterministic mock generator."""

        return SourceInfo(
            kind="mock",
            as_of="",
            geography=city.name,
            source_name="Deterministic mock data",
            source_url="",
        )


class SourcedCityDataProvider(CityDataProvider):
    """Prefer bundled sourced observations and fall back explicitly to mock data."""

    def __init__(self, data_path: Path | None = None) -> None:
        """Load the curated real-data catalog from a CSV file."""

        path = data_path or Path(__file__).parents[1] / "data" / "real_metrics.csv"
        self._fallback = MockCityDataProvider()
        self._records: dict[tuple[str, str], dict[str, str]] = {}
        with path.open(encoding="utf-8", newline="") as source_file:
            for row in csv.DictReader(source_file):
                self._records[(row["city_code"], row["metric_key"])] = row

    def fetch_metric(self, city: City, metric_key: str) -> float:
        """Return a sourced value when present, otherwise a stable mock value."""

        record = self._records.get((city.code, metric_key))
        if record is not None:
            return float(record["value"])
        return self._fallback.fetch_metric(city, metric_key)

    def source_for(self, city: City, metric_key: str) -> SourceInfo:
        """Return source metadata or an explicit mock fallback marker."""

        record = self._records.get((city.code, metric_key))
        if record is None:
            return self._fallback.source_for(city, metric_key)
        return SourceInfo(
            kind="official",
            as_of=record["as_of"],
            geography=record["geography"],
            source_name=record["source_name"],
            source_url=record["source_url"],
        )


class ApiCityDataProvider(CityDataProvider):
    """Template provider for replacing mock values with a real HTTP API."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 10.0) -> None:
        """Configure the API endpoint, credentials, and request timeout."""

        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def fetch_metric(self, city: City, metric_key: str) -> float:
        """Fetch a metric from an API expected to return ``{"value": number}``."""

        import requests

        response = requests.get(
            f"{self.base_url}/metrics/{metric_key}",
            params={"city": city.name, "country": city.country},
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=self.timeout,
        )
        response.raise_for_status()
        return float(response.json()["value"])


def fetch_crime_data(city: City, provider: CityDataProvider) -> float:
    """Fetch visitor-relevant personal and property crime data."""

    return provider.fetch_metric(city, "safety_crime_rate")


def fetch_purchasing_power_data(city: City, provider: CityDataProvider) -> float:
    """Fetch purchasing-power-parity data through the configured provider."""

    return provider.fetch_metric(city, "purchasing_power_parity")


def fetch_population_data(city: City, provider: CityDataProvider) -> float:
    """Fetch population density data through the configured provider."""

    return provider.fetch_metric(city, "population_density")
