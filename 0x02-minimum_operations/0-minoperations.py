#!/usr/bin/python3
"""
This module provides a method to calculate the minimum number of operations
needed to achieve exactly n H characters in a text editor.
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get n H's.

    Args:
        n (int): The number of H characters to achieve.

    Returns:
        int: The fewest number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0

    total_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            total_operations += factor
            n //= factor
        factor += 1
    return total_operations
