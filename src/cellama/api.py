"""Public API for CELLama."""
from __future__ import annotations

from .pipeline.embed import CellamaEmbedder
from .text.builder import SentenceBuilder
from .encoding.st_encoder import STEncoder

__all__ = ["embed", "CellamaEmbedder", "SentenceBuilder", "STEncoder"]


def embed(
    adata,
    schema: str = "basic",
    encoder: str | None = None,
    out_key: str = "X_cellama",
    **kwargs,
):
    """Embed cells and store result in ``adata.obsm[out_key]``."""
    sb = SentenceBuilder.from_schema(schema)
    enc = STEncoder.from_name(
        encoder or "sentence-transformers/all-MiniLM-L6-v2"
    )
    pipe = CellamaEmbedder(sentence_builder=sb, encoder=enc, **kwargs)
    return pipe.transform(adata, out_key=out_key)
