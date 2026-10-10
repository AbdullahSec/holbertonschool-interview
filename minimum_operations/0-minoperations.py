#!/usr/bin/python3
"""Calculate the minimum operations needed to reach n H characters."""


def minOperations(n):
    """Return the minimum number of Copy All and Paste operations."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
