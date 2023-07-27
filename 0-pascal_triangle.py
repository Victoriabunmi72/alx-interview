#!/usr/bin/python3
"""Pascal triangle."""


def pascal_triangle(n):
    """
    Get the pascal triangle of a certain power.

    Examples:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> pascal_triangle(4)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        >>> pascal_triangle(0)
        []

    Args:
        n (int): the power
    """
    if n <= 0:
        return []
    res = []
    for i in range(n):
        temp = []
        for j in range(i+1):
            temp.append(get_combination(i, j))
        res.append(temp)
    return res


def get_factorial(n):
    """
    Return the factorial for the number passed.

    Examples:
        >>> get_factorial(5)
        120
        >>> get_factorial(0)
        1

    Args:
        n (int): Target number
    Returns: factorial of n
    """
    if n == 0:
        return 1
    res: int = 1
    for i in range(n, 0, -1):
        res *= i
    return res


def get_combination(n, r):
    """
    Get the combinatation of object in set size n with respect to r.

    >>> get_combination(5, 5)
    1
    >>> get_combination(5, 4)
    5
    >>> get_combination(5, 3)
    10

    Args:
        n (int): size set
        r (int): number of object to choose from the set n at a time

    Returns: nCr
    """
    nominator = get_factorial(n)
    denominator = 0
    if (n-r) == n:
        denominator = nominator
    else:
        denominator = get_factorial(r)*get_factorial(n-r)

    return int(nominator / denominator)
