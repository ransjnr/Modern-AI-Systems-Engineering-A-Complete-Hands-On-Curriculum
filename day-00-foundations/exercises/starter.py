"""Scaffold for Exercise 1. Run: python3 starter.py"""
def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    # TODO: split, lowercase, count
    return counts

if __name__ == "__main__":
    print(word_count("the cat sat on the mat the cat"))
    # expected: {'the':3,'cat':2,'sat':1,'on':1,'mat':1}
