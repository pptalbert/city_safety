"""Ensure project modules are importable during tests."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1]))
