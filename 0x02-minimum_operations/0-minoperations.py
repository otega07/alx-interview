#!/usr/bin/python3
"""method calculates the fewest number of operations needed to result in n H
"""


def minOperations(n):
    """Calculate the minimum number of operations to get n H's"""
    if n <= 1:
        return 0
    
    total_operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            total_operations += factor  # Count the operations based on the prime factor
            n //= factor
        factor += 1
    return total_operations
