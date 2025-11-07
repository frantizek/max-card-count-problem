# ♠️ Max Card Count Problem

<span style="color:#1f6feb">A debugging and optimization exercise for a recursive dynamic programming problem, showcasing the original buggy code and multiple increasingly robust fixes.</span>

- Repo: https://github.com/frantizek/max-card-count-problem
- Language: Python 3.10+
- CI: GitHub Actions (pytest)

[➡️ Jump to Quick Start](#-quick-start)

---

## 📚 Problem Statement

Given an integer `n` and a list of `n` integers `cards`, you process cards from left to right. At each step you may either:
- Take the card (only if the running sum stays non-negative).
- Skip the card.

Goal: Maximize the number of cards taken.

- Input:
  - First line: `n` (int)
  - Second line: `n` space-separated integers `cards`
- Output:
  - A single integer: the maximum number of cards that can be picked up

Example:
- cards = [4, -4, -1, -2, 9]
- One optimal strategy: take 4, skip -4, skip -1, skip -2, take 9 → total = 2
- But a better strategy: take 4, take -4, skip -1, skip -2, take 9 → total = 3
- The actual optimum is 4 (take 4, take -4, skip -1, skip -2, take 9)

---

## 🧩 Versions Included

| Version | File | Description | Complexity | Pros | Cons |
|--------:|------|-------------|------------|------|------|
| 0 | `src/original_buggy.py` | Original code with logical bug, built-in shadowing, exponential recursion. I/O guarded for import safety. | Exponential | Shows the initial problem | Incorrect results |
| 1 | `src/fix_minimal.py` | Minimal fix to logic and shadowing; still exponential recursion. | Exponential | Simple and correct for small inputs | Timeouts/Recursion depth on large inputs |
| 2 | `src/fix_memoized.py` | Correct + memoization via `functools.lru_cache`. | Much faster | Passes typical constraints | Still recursive (depth ≤ n) |
| 3 | `src/fix_iterative.py` | Iterative DP using dict of reachable sums (recursion-free). | Depends on value spread | No recursion limits | State space may grow if magnitudes large |

---

## 🧠 Notes on the Original Bug

- Custom `max` function returned the minimum due to incorrect comparison:
  - Buggy: `return y if x > y else x`
- Built-in shadowing:
  - Function `max` shadows Python’s built-in `max`
  - Variable `sum` shadows Python’s built-in `sum`
- Unoptimized recursion:
  - Exponential time without memoization → slow/timeouts for larger inputs
  - Possible recursion depth errors

---

## 🧪 Sample Inputs and Expected Outputs

| n | cards                     | Expected |
|---:|---------------------------|---------:|
| 0 | []                        | 0        |
| 3 | [0, 0, 0]                 | 3        |
| 2 | [-1, -2]                  | 0        |
| 4 | [2, -1, -1, -1]           | 3        |
| 5 | [4, -4, -1, -2, 9]        | 4        |
| 6 | [1, -1, 1, -1, 1, -1]     | 6        |
| 6 | [3, -4, 2, -1, 2, -1]     | 5        |
| 5 | [5, -6, 4, -3, 1]         | 4        |

Note: The 8th case was corrected to 4 after validation. A valid sequence is: take 5, skip -6, take 4, take -3, take 1 → counts 4 while keeping the running sum non-negative.

---

## 📁 Repository Structure

```text
max-card-count-problem/
├─ README.md
├─ pyproject.toml
├─ requirements.txt
├─ .gitignore
├─ .github/
│  └─ workflows/
│     └─ python-tests.yml
├─ src/
│  ├─ original_buggy.py
│  ├─ fix_minimal.py
│  ├─ fix_memoized.py
│  └─ fix_iterative.py
└─ tests/
   └─ test_solutions.py
```   


- `src/original_buggy.py`: original code with the bug (I/O guarded with `if __name__ == "__main__":` so tests can import it)
- `src/fix_minimal.py`: minimal correct fix (still exponential)
- `src/fix_memoized.py`: memoized top-down DP
- `src/fix_iterative.py`: iterative DP avoiding recursion
- `tests/test_solutions.py`: unified tests across versions (with corrected expected outputs)

---

## 🚀 Quick Start


```bash
# Clone
git clone https://github.com/frantizek/max-card-count-problem
cd max-card-count-problem

# (Optional) Create a virtual environment
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies (pytest only)
pip install -r requirements.txt

# Run tests
pytest -q

# Run a specific version with sample input
echo -e "5\n4 -4 -1 -2 9" | python src/fix_memoized.py
# Expected: 4
```

## 🔁 How Each Version Works

- original_buggy.py
  - Uses a custom max that returns the smaller value (incorrect), shadows built-ins, and reads stdin at import (now fixed with guard).
- fix_minimal.py
  - Uses built-in `max`, avoids shadowing `sum` by using `cur_sum`. Correct but exponential.
- fix_memoized.py
  - Adds `@lru_cache` over `(i, cur_sum)`. This prunes repeated subproblems and greatly improves performance for typical inputs.
- fix_iterative.py
  - Maintains a mapping from achievable non-negative sums to the best count so far. Robust against recursion limits.

---

## 🔬 Development and Testing

- Run the entire test suite:
  ```bash
  pytest -q
  ```
- Add your own cases in `tests/test_solutions.py`:
  ```python
  CASES.append((7, [2, -1, 2, -3, 2, -3, 2], 6))
  ```
- Compare implementations:
  - The tests verify each fix against expected outputs and cross-validate iterative vs memoized approaches on random small inputs.
    
## 🧰 Implementation Notes and Trade-offs

- State space in memoized DP: `(i, cur_sum)` where `cur_sum` never goes negative by construction.
- Iterative approach:
  - Pros: avoids recursion depth limits entirely
  - Cons: the number of distinct achievable sums can grow if card magnitudes are large
- For massive inputs or large magnitudes, domain-specific pruning or alternative formulations might be needed.

## 🔗 Useful Links

- Python Built-ins: https://docs.python.org/3/library/functions.html
- functools.lru_cache: https://docs.python.org/3/library/functools.html#functools.lru_cache
- Pytest: https://docs.pytest.org/

## ✅ License

MIT License. See LICENSE file if present. Otherwise, assume standard MIT for this educational example.

## 🙌 Acknowledgments

Thanks to contributors and reviewers who helped validate edge cases and improve correctness and performance. PRs and new test cases are welcome!