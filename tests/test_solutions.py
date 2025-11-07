# tests/test_solutions.py
import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

buggy = importlib.import_module("original_buggy")
fix_minimal = importlib.import_module("fix_minimal")
fix_memoized = importlib.import_module("fix_memoized")
fix_iterative = importlib.import_module("fix_iterative")

def run_mod(mod, n, cards):
    if hasattr(mod, "max_card_count"):
        return mod.max_card_count(n, cards)
    # fallback for original_buggy API
    return mod.maxCardCount(n, cards)

CASES = [
    (0, [], 0),
    (3, [0, 0, 0], 3),
    (2, [-1, -2], 0),
    (4, [2, -1, -1, -1], 3),
    (5, [4, -4, -1, -2, 9], 4),
    (6, [1, -1, 1, -1, 1, -1], 6),
    (6, [3, -4, 2, -1, 2, -1], 5),
    (5, [5, -6, 4, -3, 1], 4),
]

def test_minimal_vs_memoized():
    for n, cards, expected in CASES:
        assert run_mod(fix_minimal, n, cards) == expected

def test_memoized_expected():
    for n, cards, expected in CASES:
        assert run_mod(fix_memoized, n, cards) == expected

def test_iterative_expected():
    for n, cards, expected in CASES:
        assert run_mod(fix_iterative, n, cards) == expected

def test_iterative_vs_memoized_random_small():
    import random
    random.seed(0)
    for _ in range(200):
        n = random.randint(0, 10)
        cards = [random.randint(-5, 5) for _ in range(n)]
        r1 = run_mod(fix_memoized, n, cards)
        r2 = run_mod(fix_iterative, n, cards)
        assert r1 == r2