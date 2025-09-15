"""Encoding interfaces."""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Sequence


class Encoder(ABC):
    @abstractmethod
    def encode(self, texts: List[str], batch_size: int = 32) -> Sequence[Sequence[float]]:
        ...
