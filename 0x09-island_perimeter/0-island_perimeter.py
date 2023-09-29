#!/usr/bin/python3
"""
Calculates Island perimeter
"""


def island_perimeter(grid):
    """
    Uses a matrix of 1 and 0 to calculate perimeter
    - The 0 represents water and 1 represents land
    - There is either an island or no island
    - No lakes are present (No 0 in middle of 1's)
    """
    perimeter = 0
    if type(grid) is not list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            land = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(land)
    return perimeter
