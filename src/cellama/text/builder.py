"""Sentence building utilities."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class SentenceBuilderConfig:
    top_k_genes: int = 50
    include_neighbors: bool = True
    template: str = "basic"


class SentenceBuilder:
    """Build sentences from AnnData."""

    def __init__(self, cfg: SentenceBuilderConfig):
        self.cfg = cfg

    def build(self, adata) -> List[str]:
        # TODO: integrate real logic
        return [f"cell {i} with top genes ..." for i in range(adata.n_obs)]

    @classmethod
    def from_schema(cls, name: str) -> "SentenceBuilder":
        # TODO: load schema-specific config
        return cls(SentenceBuilderConfig())
