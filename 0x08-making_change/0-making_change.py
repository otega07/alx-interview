#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order once
    coins.sort(reverse=True)
    change = 0

    # Iterate through each coin and use as many as possible
    for coin in coins:
        if coin <= total:
            num_of_coins = total // coin
            change += num_of_coins
            total -= coin * num_of_coins

        if total == 0:
            return change

    return -1
