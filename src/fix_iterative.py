# src/fix_iterative.py
"""
Iterative (recursion-free) implementation of the "Max Card Count" problem.

Summary:
- Correct solution without recursion (avoids recursion depth limits).
- Avoids shadowing built-ins (uses `cur_sum` conceptually but we store sums as keys).
- Maintains a mapping of achievable non-negative sums to the maximum number of
  cards that can be taken to achieve each sum after processing a prefix of cards.

Problem (informal):
- Given n integers (cards), processed left-to-right.
- At each step, you may take or skip the card.
- You may only take a card if the running sum remains non-negative.
- Goal: maximize the number of cards taken.

Key idea:
- Let dp be a dictionary mapping: sum_value -> best_count
  where sum_value >= 0 and best_count is the maximum number of cards taken to
  achieve sum_value after processing some prefix of the cards.
- Initialize dp = {0: 0} (sum 0 with 0 cards taken before processing any cards).
- For each card c:
    - Start with new_dp = dict(dp) (skipping c preserves all existing states).
    - For every (s, cnt) in dp:
        - If s + c >= 0, we can "take" c and reach new sum ns = s + c with count cnt + 1.
        - Update new_dp[ns] = max(new_dp.get(ns, -inf), cnt + 1).
    - Set dp = new_dp for the next iteration.
- The answer is max(dp.values()).

Complexity:
- Time: O(n * K) where K is the number of distinct achievable sums encountered.
  K depends on card magnitudes and distribution.
- Space: O(K).
- In practice, this is efficient for moderate inputs and avoids recursion issues.

Trade-offs:
- Compared to memoized recursion, this approach avoids recursion depth limits entirely.
- However, if many sums are achievable (e.g., large magnitudes, varied combinations),
  the dictionary can grow. Memoized recursion may be preferable if (i, cur_sum) states
  are sparser for your data.

I/O behavior:
- Input is read only under `if __name__ == "__main__":` to allow safe importing in tests.
"""

from typing import Dict, List


def max_card_count(n: int, cards: List[int]) -> int:
    """
    Compute the maximum number of cards that can be picked up using an iterative
    dynamic programming approach over achievable non-negative sums.

    Parameters:
        n (int): Number of cards. Expected to equal len(cards).
        cards (List[int]): The list of card values to process in order.

    Returns:
        int: The maximum number of cards that can be taken while maintaining a
             non-negative running sum at all times.
    """
    # dp maps achievable non-negative sums to the best count of cards taken.
    dp: Dict[int, int] = {0: 0}

    for c in cards:
        # Begin with the "skip" option: retain all existing states.
        new_dp: Dict[int, int] = dict(dp)

        # Consider "take" option for each existing achievable sum.
        for s, cnt in dp.items():
            ns = s + c
            if ns >= 0:
                # If we can take this card, update the new mapping with the improved count.
                new_cnt = cnt + 1
                # Only keep the best count for a given sum.
                if ns not in new_dp or new_dp[ns] < new_cnt:
                    new_dp[ns] = new_cnt

        # Move to the next card with updated states.
        dp = new_dp

    # If no states exist (shouldn't happen since {0:0} persists), default to 0.
    return max(dp.values()) if dp else 0


if __name__ == "__main__":
    # Read input (n, then the list of cards) only when executed as a script.
    n = int(input().strip())
    cards = list(map(int, input().split()))
    print(max_card_count(n, cards))