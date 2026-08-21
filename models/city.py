"""City domain model."""

from dataclasses import dataclass


@dataclass(frozen=True)
class City:
    """Identify a city and its country."""

    country: str
    name: str
    code: str
