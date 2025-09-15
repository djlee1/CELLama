"""CLI entrypoints for CELLama."""
from __future__ import annotations

import typer

from .api import embed
from .data.io import read_h5ad, write_h5ad

app = typer.Typer()


@app.command()
def run(
    input: str,
    output: str = "output.h5ad",
    schema: str = "basic",
    encoder: str = "sentence-transformers/all-MiniLM-L6-v2",
    out_key: str = "X_cellama",
):
    """Run embedding on an input file."""
    adata = read_h5ad(input)
    embed(adata, schema=schema, encoder=encoder, out_key=out_key)
    write_h5ad(adata, output)


@app.command()
def train(config: str) -> None:
    """Placeholder training command."""
    typer.echo(f"Training with config {config} not implemented")


def main() -> None:
    app()


if __name__ == "__main__":  # pragma: no cover
    main()
