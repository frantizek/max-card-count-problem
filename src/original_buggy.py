# src/original_buggy.py
"""
Original (buggy) implementation of the "Max Card Count" problem.

This module intentionally preserves the original logic and its defects
for educational purposes. It adds comprehensive documentation and comments
to make the behavior, inputs/outputs, and the specific bug easier to
understand and test against.

Problem (informal):
- You are given n integers (cards), processed left-to-right.
- You may take or skip each card.
- You may only take a card if the running sum remains non-negative.
- Goal: maximize the number of taken cards.

Known issues in this original code:
1) The custom `max` function is incorrect. It returns the minimum of (x, y)
   instead of the maximum. This leads to suboptimal or incorrect results.
2) The variable name `sum` shadows Python's built-in `sum` function.
   While it does not break this specific script, it is poor practice and can
   cause confusion or conflicts in larger programs.
3) The approach uses naive recursion without memoization, resulting in
   exponential time complexity and potential recursion depth issues for large inputs.

I/O behavior:
- Input is read only when the module is executed as a script (via __main__)
  so that importing this module in tests does not block on stdin.
"""

def maxCardCount(n: int, card: list[int]) -> int:
    """
    Compute the maximum number of cards that can be picked up, according to the
    original (buggy) implementation.

    Parameters:
        n (int): Number of cards. Expected to match len(card).
        card (list[int]): The list of card values to consider, processed in order.

    Returns:
        int: The computed maximum number of cards (may be incorrect due to the
             bug in the custom `max` function below).

    Notes:
        - Delegates to the recursive helper `dp` starting from index 0
          with an initial running sum of 0.
        - This function is left intentionally unchanged to preserve the original bug.
    """
    return dp(0, n, card, 0)


def dp(i: int, n: int, card: list[int], sum: int) -> int:
    """
    Recursive subproblem for the original implementation.

    Parameters:
        i (int): Current index in the card list.
        n (int): Total number of cards.
        card (list[int]): The list of card values.
        sum (int): Current running sum (non-negative is required when taking a card).

    Returns:
        int: The maximum number of cards that can be taken from position i onward,
             as computed by the original (buggy) recursion.

    Behavior:
        - Base case: if i == n, no more cards → return 0.
        - If taking card[i] does not make the sum negative, the recursion
          considers both taking and skipping the card.
        - Otherwise, it must skip the card.

    Important:
        - This function calls the custom `max` defined below, which is buggy and
          returns the MINIMUM instead of the MAXIMUM. This is the central bug
          of the original code.
        - Variable name `sum` shadows the built-in, kept here to preserve the
          original structure and demonstrate the issue.
    """
    if i == n:
        # No more cards to process.
        return 0
    elif sum + card[i] >= 0:
        # Option 1: Take the card (count +1), move to next index with updated sum.
        # Option 2: Skip the card, keep the same sum and move to next index.
        # BUG PROPAGATION: uses the buggy `max` function below.
        return max(
            1 + dp(i + 1, n, card, sum + card[i]),
            dp(i + 1, n, card, sum),
        )
    else:
        # Cannot take the card because it would make the running sum negative.
        return dp(i + 1, n, card, sum)


def max(x, y):
    """
    BUGGY custom `max` function.

    This function is intended to return the larger of x and y, but due to the
    incorrect comparison, it actually returns the smaller value, i.e., the MIN.

    Parameters:
        x: Comparable value.
        y: Comparable value.

    Returns:
        The smaller of x and y (incorrect behavior).

    Correct version (NOT used here to preserve the original bug):
        def max(x, y):
            return y if y > x else x
    """
    # BUG: returns min instead of max
    return y if x > y else x


if __name__ == "__main__":
    # Read input values only when executed as a script (not when imported by pytest)
    n = int(input().strip())
    cards = list(map(int, input().split()))

    # Compute result using the original (buggy) implementation
    result = maxCardCount(n, cards)

    # Print the result (may be incorrect due to the custom `max` bug)
    print(result)