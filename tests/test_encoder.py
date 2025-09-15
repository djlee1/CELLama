from cellama.encoding.st_encoder import STEncoder


def test_encoder_shape():
    enc = STEncoder.from_name("sentence-transformers/paraphrase-MiniLM-L3-v2")
    vecs = enc.encode(["hello", "world"], batch_size=2)
    assert len(vecs) == 2
    assert len(vecs[0]) == len(vecs[1])
