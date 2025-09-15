# CELLama

CELLama converts single-cell data into language model embeddings.

```python
from cellama import embed
import anndata as ad
adata = ad.AnnData(X=[[0,1],[1,0]])
embed(adata)
```
