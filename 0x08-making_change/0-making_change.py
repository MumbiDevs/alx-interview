#!/usr/bin/python3
"""
Module for the makeChange function
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: Minimum number of coins needed to achieve the total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total of 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
