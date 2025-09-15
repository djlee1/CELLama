"""Parallel utilities."""
from __future__ import annotations

from multiprocessing import Pool
from typing import Iterable, Callable, Any


def map_parallel(func: Callable[[Any], Any], iterable: Iterable[Any], workers: int = 1):
    if workers <= 1:
        return [func(x) for x in iterable]
    with Pool(workers) as pool:
        return pool.map(func, iterable)
