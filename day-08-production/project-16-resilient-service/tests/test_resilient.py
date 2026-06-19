from app.cache import lookup, store

def test_exact_cache_hit():
    store("ping?", "pong")
    ans, how = lookup("PING?")          # case-insensitive key
    assert ans == "pong" and how == "exact"

def test_miss_on_unknown():
    ans, how = lookup("a truly unseen question 8472")
    assert ans is None and how == "miss"
