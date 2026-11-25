#!/usr/bin/python3


def isWinner(x, nums):
    max_n = max(nums)

    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for number in range(2, max_n + 1):
        if is_prime[number]:
            for multiple in range(number * 2, max_n + 1, number):
                is_prime[multiple] = False

    prime_count = [0] * (max_n + 1)

    for n in range(2, max_n + 1):
        prime_count[n] = prime_count[n - 1]
        if is_prime[n]:
            prime_count[n] += 1

    maria_wins = 0
    ben_wins = 0