# 0x09. Island Perimeter
Algorithm
Python

For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.

## Concepts Needed:

### 2D Arrays (Matrices):

Accessing and iterating over elements in a 2D array.

Understanding how to navigate through adjacent cells (horizontally and vertically).

### Conditional Logic:

Applying conditions to determine whether a cell contributes to the perimeter of the island.

### Counting Techniques:

Developing a method to count the edges that contribute to the island’s perimeter.

### Problem-Solving Strategies:

Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.

### Python Programming:

Nested loops for iterating over grid cells.

Conditional statements to check the status of adjacent cells.

## Resources:

### Python Official Documentation:

Nested Lists [https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions]: Understanding how to work with lists within lists in Python.

### GeeksforGeeks Articles:

Python Multi-dimensional [https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/]: A guide to working with 2D arrays in Python effectively.

### TutorialsPoint:

Python Lists [https://www.tutorialspoint.com/python/python_lists.htm]: Explains how to create, access, and manipulate lists in Python, which is essential for working with a grid.

### YouTube Tutorials:

Python 2D arrays and lists [https://www.youtube.com/watch?v=aNzepGawwCI]


By understanding these concepts and utilizing the provided resources, you will be equipped to approach the problem methodically. You’ll need to iterate over the grid, apply logical operations to identify the perimeter of the island, and account for the specific conditions described in the task. This project not only tests your algorithmic thinking but also reinforces your ability to manipulate data structures and apply logical reasoning to solve problems.

## Additional Resources

Mock Technical Interviews [https://www.youtube.com/watch?v=fFgEM6CMQc4]

## Requirements

Allowed editors: vi, vim, emacs

All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)

All your files should end with a new line

The first line of all your files should be exactly #!/usr/bin/python3

A README.md file, at the root of the folder of the project, is mandatory

Your code should use the PEP 8 style (version 1.7)

You are not allowed to import any module

All modules and functions must be documented

All your files must be executable

## Task

task is about creating a function called island_perimeter(grid) that calculates the perimeter of an island represented in a 2D grid. In this grid, 0 represents water and 1 represents land. The function needs to count the number of edges of the land cells (1s) that are adjacent to water cells (0s) or the edge of the grid, as each edge contributes to the perimeter. The grid is guaranteed to be surrounded by water, and there is only one island without any enclosed water (lakes). The output is the total perimeter length of the island.
