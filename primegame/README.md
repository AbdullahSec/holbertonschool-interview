# Prime Game

Determine whether Maria or Ben wins the most rounds of a prime number game.

## Rules

- Each round starts with the integers from `1` to `n`.
- Maria plays first.
- Players take turns removing a prime number and its multiples.
- A player who cannot make a move loses.

## Function

```python
def isWinner(x, nums):
```

- `x`: Number of rounds.
- `nums`: List of upper limits for the rounds.
- Returns `"Maria"` or `"Ben"` for the player with more wins.
- Returns `None` if no overall winner can be determined.

## Approach

Use the Sieve of Eratosthenes to identify primes and cumulative counts to count primes up to each round's limit. An odd count means Maria wins; an even count means Ben wins.

## Constraints

- No package imports.
- `x` and `n` do not exceed `10000`.