#!/usr/bin/python3
"""Calculate the perimeter of an island in a rectangular grid."""


def island_perimeter(grid):
    """Return the perimeter of the single island represented by grid."""
    perimeter = 0
    height = len(grid)
    width = len(grid[0]) if height else 0

    for row in range(height):
        for column in range(width):
            if grid[row][column] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][column] == 1:
                    perimeter -= 2
                if column > 0 and grid[row][column - 1] == 1:
                    perimeter -= 2

    return perimeter
