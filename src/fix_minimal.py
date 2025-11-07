# src/fix_minimal.py
"""
Minimal corrected implementation of the "Max Card Count" problem.

This version focuses on the smallest set of changes required to obtain correct
results compared to the original buggy script:
- Uses Python's built-in `max` (does not redefine it).
- Avoids shadowing Python built-ins by renaming `sum` -> `cur_sum`.
- Keeps the same top-down recursive structure for clarity and proximity to
  the original code.

Caveats:
- This solution is still exponential time in the worst case because it does not
  use memoization. It is therefore suitable only for small inputs. See
  `src/fix_memoized.py` or `src/fix_iterative.py` for efficient alternatives.

Problem (informal):
- Given n integers (cards), processed left-to-right.
- At each step, you may take or skip the card.
- You may only take a card if the running sum remains non-negative.
- Goal: maximize the number of cards taken.

I/O behavior:
- Input is read only under `if __name__ == "__main__":` to allow safe importing in tests.
"""

from typing import List


def max_card_count(n: int, cards: List[int]) -> int:
    """
    Compute the maximum number of cards that can be picked up.

    Parameters:
        n (int): Number of cards. Expected to equal len(cards).
        cards (List[int]): The list of card values to process in order.

    Returns:
        int: The maximum number of cards that can be taken while keeping the
             running sum non-negative at all times.

    Notes:
        - This is a minimal fix: no memoization; recursion is exponential.
        - For large inputs, prefer the memoized or iterative versions.
    """

    def dp(i: int, cur_sum: int) -> int:
        """
        Recursive helper.

        Parameters:
            i (int): Current index in the card list (0-based).
            cur_sum (int): Current running sum (must remain >= 0 whenever a card is taken).

        Returns:
            int: Best achievable count from index i onward.
        """
        # Base case: no more cards to consider.
        if i == n:
            return 0

        # Option 1: take the card if it keeps the sum non-negative.
        take_count = -1
        nxt_sum = cur_sum + cards[i]
        if nxt_sum >= 0:
            take_count = 1 + dp(i + 1, nxt_sum)

        # Option 2: skip the card.
        skip_count = dp(i + 1, cur_sum)

        # Choose the better of the two options.
        return max(take_count, skip_count)

    return dp(0, 0)


if __name__ == "__main__":
    # Read input (n, then the list of cards) only when executed as a script.
    n = int(input().strip())
    cards = list(map(int, input().split()))
    print(max_card_count(n, cards))