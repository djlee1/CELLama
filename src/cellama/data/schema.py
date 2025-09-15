"""Schema validation utilities."""
from __future__ import annotations

from anndata import AnnData


def validate_basic(adata: AnnData) -> None:
    """Placeholder schema validation."""
    if adata.X is None:
        raise ValueError("adata.X is required")
