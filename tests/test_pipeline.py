from cellama.pipeline.embed import CellamaEmbedder
from cellama.text.builder import SentenceBuilder
from cellama.encoding.st_encoder import STEncoder


def test_pipeline_end_to_end(adata):
    sb = SentenceBuilder.from_schema("basic")
    enc = STEncoder.from_name("sentence-transformers/paraphrase-MiniLM-L3-v2")
    pipe = CellamaEmbedder(sb, enc)
    X = pipe.transform(adata)
    assert len(X) == adata.n_obs
