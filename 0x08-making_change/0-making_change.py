#!/usr/bin/python3
""" Make change
"""


from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """ make Change

    Args:
        coins (List[int]): List of coins
        total (int): Total coin

    Returns:
        int: fewest coin combination to make the total coin
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    fewest_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            fewest_coins += 1
    if total == 0:
        return fewest_coins
    return -1
