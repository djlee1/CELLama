from cellama import embed


def test_embed_adds_obsm(adata):
    X = embed(adata, schema="basic", out_key="X_cellama")
    assert "X_cellama" in adata.obsm
    assert len(X) == adata.n_obs
