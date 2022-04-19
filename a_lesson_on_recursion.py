#!/usr/bin/python
# PROGRAMMER: Luke Wilson
##

"""
Process for developing recursion:
1. What is the simplest possible base case
2. Code the base case where we return
3. Create simple examples and look at what happens
4. Review what changes at each step to look for pattern
5. Generalize the pattern
6. Code the recursive pattern to return the pattern
"""

# Recursion
# Example: Fibonacci
class Solution:
    def fib(self, n: int, total = 0, previous = 1, i = 0) -> int:
        # Recursive Call (Tunneling backward and then returning upward)
        if n <= 1: return n
        return Solution.fib(self, n-1) + Solution.fib(self, n-2) # (Repeat counting)

        # Dynamic Programming (Counting upward, much more efficient)
        if i >= n: return total
        temp = total
        total = total + previous
        previous = temp
        return Solution.fib(self, n, total, previous, i + 1)

        # Math Cheat
        return int((((1 + 5 ** 0.5) / 2) ** n + 1) / 5 ** 0.5)

    def fib_bottom_up_iterative(n):
        # Dynamic Programming Bottom Up Iterative
        if n <= 1: return n
        small = 0
        large = 1
        total = 0
        for i in range(n-1):
            total = small + large
            small = large
            large = total
        return total


# Example: Sum Numbers
class Solution:
    def sumTo (n):
        if (n == 0): return 0
        return sumTo(n-1) + n



# Example: Find the Total Number of Islands (Iterative Approach)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Create a list of directions to take to scan neighbouring indices
        move = [[0,-1],[0,1],[-1,0],[1,0]]

        # Initialize the number of columns and rows, consider that range drops last value
        cols = range(len(grid[0]))
        rows = range(len(grid))

        # Initialize an empty set to track locations that have been checked, like dicts, sets are O(1) lookup
        checked = set()
        islands = 0


        # Create a recursive search function, that will propogate outward across an island to check all ones
        def search_island(coordinates):

            # Initialize a deque using the found starting point coordinates, a deque can be popped at O(1) speed
            search_tasks = collections.deque([coordinates])

            # Loop through a search, popping a new location from the deque, searching neighbouring locations, checking if
            # locations have been checked yet,adding any unchecked prospective land back to the deque, and continuing search
            while search_tasks:
                x, y = search_tasks.pop()

                # Check all possible neighbours at the given popped location for unchecked land, add to search and checked
                for Δx, Δy in move:
                    row, col = x + Δx, y + Δy
                    if row in rows and col in cols and grid[row][col] == '1' and (row, col) not in checked:
                        search_tasks.append((row, col))
                        checked.add((row, col))

        # Now that we have a recursive search, we iterate through the grid for unchecked land and search when land is found
        for row in rows:
            for col in cols:
                # If it's land that hasn't been checked, we start a search, then add it to checked and add an island to count
                if grid[row][col] == '1' and (row, col) not in checked:
                    search_island((row, col))
                    checked.add((row, col))
                    islands += 1

        return islands
