# Making Change

The makeChange(coins, total) function returns the minimum number of coins
needed to form total, or -1 when the amount cannot be formed. It uses
dynamic programming: for each amount, it considers each denomination and
reuses the best result for the remaining amount.

The runtime is O(total * len(coins)), and the extra space is O(total).
