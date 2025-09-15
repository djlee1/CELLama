"""Sentence-Transformers backend encoder."""
from __future__ import annotations

import hashlib
from typing import List

from .base import Encoder

try:  # pragma: no cover
    from sentence_transformers import SentenceTransformer
except Exception:  # pragma: no cover
    SentenceTransformer = None  # type: ignore


class STEncoder(Encoder):
    """Encoder using `sentence-transformers` models."""

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        if SentenceTransformer is not None:
            self.model = SentenceTransformer(model_name)
        else:
            self.model = None

    def encode(self, texts: List[str], batch_size: int = 32):  # pragma: no cover
        if self.model is None:
            # Deterministic hash-based embeddings
            return [
                [b / 255 for b in hashlib.sha256(t.encode()).digest()]
                for t in texts
            ]
        return self.model.encode(texts, batch_size=batch_size, convert_to_numpy=False)

    @classmethod
    def from_name(cls, name: str) -> "STEncoder":
        return cls(model_name=name)
