"""Configuration schemas."""
from __future__ import annotations

from pydantic import BaseModel


class EmbedConfigModel(BaseModel):
    batch_size: int = 64
    cache: bool = True
