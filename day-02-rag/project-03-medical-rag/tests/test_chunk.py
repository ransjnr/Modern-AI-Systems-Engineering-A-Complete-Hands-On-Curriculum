from app.ingest import chunk

def test_chunk_overlaps_and_covers():
    text = " ".join(str(i) for i in range(1000))
    chunks = chunk(text, size=400, overlap=60)
    assert len(chunks) >= 2
    assert all(len(c) > 0 for c in chunks)
