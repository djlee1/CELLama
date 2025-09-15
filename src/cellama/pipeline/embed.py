"""Embedding pipeline."""
from __future__ import annotations

from dataclasses import dataclass

from ..encoding.base import Encoder
from ..text.builder import SentenceBuilder


@dataclass
class EmbedConfig:
    batch_size: int = 64
    cache: bool = True


class CellamaEmbedder:
    def __init__(
        self,
        sentence_builder: SentenceBuilder,
        encoder: Encoder,
        cfg: EmbedConfig | None = None,
    ):
        self.sb = sentence_builder
        self.enc = encoder
        self.cfg = cfg or EmbedConfig()

    def transform(self, adata, out_key: str = "X_cellama"):
        texts = self.sb.build(adata)
        X = self.enc.encode(texts, batch_size=self.cfg.batch_size)
        adata.obsm[out_key] = X
        return X
