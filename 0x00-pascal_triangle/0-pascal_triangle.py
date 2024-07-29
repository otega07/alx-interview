#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's Triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = []
        C = 1
        for j in range(i + 1):
            row.append(C)
            if j < i:
                C = C * (i - j) // (j + 1)
        triangle.append(row)

    return triangle
