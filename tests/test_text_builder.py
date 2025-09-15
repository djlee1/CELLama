from cellama.text.builder import SentenceBuilder


def test_sentence_builder_basic(adata):
    sb = SentenceBuilder.from_schema("basic")
    texts = sb.build(adata)
    assert len(texts) == adata.n_obs
    assert all(isinstance(t, str) for t in texts)
