# CELLama

A library for embedding single-cell expression data using language models.

## Installation

```bash
pip install cellama
```

## Quick Start

```python
from cellama import embed
import anndata as ad
adata = ad.AnnData(X=[[0,1],[1,0]])
embed(adata)
print(adata.obsm['X_cellama'])
```

## CLI

```bash
cellama run --input data.h5ad --schema basic
```
