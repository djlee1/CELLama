"""Simple caching utilities."""
from __future__ import annotations

from functools import lru_cache


@lru_cache(maxsize=1024)
def text_cache(text: str) -> str:
    return text
