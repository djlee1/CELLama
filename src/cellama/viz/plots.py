"""Visualization helpers (placeholder)."""
from __future__ import annotations

import matplotlib.pyplot as plt
from typing import Sequence


def scatter(X: Sequence[Sequence[float]]) -> None:
    xs = [row[0] for row in X]
    ys = [row[1] for row in X]
    plt.scatter(xs, ys)
    plt.show()
