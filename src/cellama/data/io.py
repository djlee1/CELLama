"""Data input/output helpers."""
from __future__ import annotations

from anndata import AnnData
import anndata as ad


def read_h5ad(path: str) -> AnnData:
    """Read an AnnData object from an ``.h5ad`` file."""
    return ad.read_h5ad(path)


def write_h5ad(adata: AnnData, path: str) -> None:
    """Write an AnnData object to ``path``."""
    adata.write_h5ad(path)
