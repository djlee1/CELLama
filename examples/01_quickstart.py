"""Quickstart example for CELLama."""
import random

from cellama import embed

random.seed(0)
X = [[random.random() for _ in range(3)] for _ in range(4)]

class SimpleAnnData:
    def __init__(self, X):
        self.X = X
        self.n_obs = len(X)
        self.obs = {}
        self.var = {}
        self.obsm = {}

adata = SimpleAnnData(X)
embed(adata)
print(len(adata.obsm["X_cellama"]))
