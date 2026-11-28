#!/usr/bin/python3
"""Determine the overall winner of the prime game."""


def isWinner(x, nums):
    """Return the player who wins the most rounds, or None for a tie."""
    if x < 1 or not nums:
        return None

    rounds = nums[:x]
    max_n = max(1, max(rounds))
    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for number in range(2, max_n + 1):
        if is_prime[number]:
            for multiple in range(number * number, max_n + 1, number):
                is_prime[multiple] = False

    prime_count = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        prime_count[n] = prime_count[n - 1] + is_prime[n]

    maria_wins = 0
    ben_wins = 0
    for n in rounds:
        if prime_count[n] % 2:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
