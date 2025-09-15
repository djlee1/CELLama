"""Configuration loader."""
from __future__ import annotations

from pathlib import Path
import yaml

from .types import EmbedConfigModel


def load_embed_config(path: str | Path) -> EmbedConfigModel:
    with open(path) as fh:
        data = yaml.safe_load(fh) or {}
    return EmbedConfigModel(**data)
