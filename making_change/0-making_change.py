#!/usr/bin/python3
"""Compute the minimum number of coins needed to make an amount."""


def makeChange(coins, total):
    """Return the fewest coins needed to make total, or -1 if impossible."""
    if total <= 0:
        return 0

    minimum = [0] + [float("inf")] * total
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                minimum[amount] = min(minimum[amount],
                                      minimum[amount - coin] + 1)

    return -1 if minimum[total] == float("inf") else minimum[total]
