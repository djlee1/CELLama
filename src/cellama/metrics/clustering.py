"""Clustering metrics (placeholder)."""
from __future__ import annotations

from typing import Sequence


def silhouette_score(X: Sequence[Sequence[float]]) -> float:
    """Return a dummy silhouette score."""
    if not X:
        return 0.0
    total = sum(sum(row) for row in X)
    count = sum(len(row) for row in X)
    return total / count
