import random
import pytest


class SimpleAnnData:
    def __init__(self, X):
        self.X = X
        self.n_obs = len(X)
        self.obs = {}
        self.var = {}
        self.obsm = {}


@pytest.fixture
def adata():
    random.seed(0)
    X = [[random.random() for _ in range(3)] for _ in range(4)]
    return SimpleAnnData(X)
