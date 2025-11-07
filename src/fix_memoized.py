# src/fix_memoized.py
"""
Memoized (top-down DP) implementation of the "Max Card Count" problem.

Summary:
- Corrects the original logical bug (uses Python's built-in max).
- Avoids shadowing built-ins (uses `cur_sum` instead of `sum`).
- Applies memoization via functools.lru_cache to eliminate redundant subproblems.
- Time complexity is greatly reduced relative to the naive recursion.

Problem (informal):
- Given n integers (cards), processed left-to-right.
- At each step, you may take or skip the card.
- You may only take a card if the running sum remains non-negative.
- Goal: maximize the number of cards taken.

Key idea:
- Define dp(i, cur_sum) = best result (max count) from index i with current sum cur_sum.
- Transitions:
    - Skip: dp(i+1, cur_sum)
    - Take: if cur_sum + cards[i] >= 0, then 1 + dp(i+1, cur_sum + cards[i])
- Answer is dp(0, 0).

Trade-offs:
- The memoized state space depends on the variety of reachable (i, cur_sum) pairs.
  In typical competitive-programming constraints, this is efficient. However, if
  card magnitudes are very large and many sums are reachable, the state space can grow.
  In such cases, see the iterative version (src/fix_iterative.py), which uses a dictionary
  keyed by sums observed at each position and avoids deep recursion.

I/O behavior:
- Input is read only under `if __name__ == "__main__":` to allow safe importing in tests.
"""

from functools import lru_cache
from typing import List


def max_card_count(n: int, cards: List[int]) -> int:
    """
    Compute the maximum number of cards that can be picked up using a memoized
    top-down DP approach.

    Parameters:
        n (int): Number of cards. Expected to equal len(cards).
        cards (List[int]): The list of card values to process in order.

    Returns:
        int: The maximum number of cards that can be taken while maintaining a
             non-negative running sum at all times.
    """

    @lru_cache(maxsize=None)
    def dp(i: int, cur_sum: int) -> int:
        """
        Memoized recursive subproblem.

        Parameters:
            i (int): Current index in the card list (0-based).
            cur_sum (int): Current running sum (must remain >= 0 whenever a card is taken).

        Returns:
            int: Best achievable count from index i onward.
        """
        # Base case: no more cards.
        if i == n:
            return 0

        # Option 1: skip the current card.
        best_skip = dp(i + 1, cur_sum)

        # Option 2: take the current card if valid.
        best_take = -1
        nxt = cur_sum + cards[i]
        if nxt >= 0:
            best_take = 1 + dp(i + 1, nxt)

        return max(best_take, best_skip)

    return dp(0, 0)


if __name__ == "__main__":
    # Read input (n, then the list of cards) only when executed as a script.
    n = int(input().strip())
    cards = list(map(int, input().split()))
    print(max_card_count(n, cards))