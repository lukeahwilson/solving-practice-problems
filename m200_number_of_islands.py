#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-17
# Question:
#       Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the
#    number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or
#    vertically. You may assume all four edges of the grid are all surrounded by water.
# Example:
#       Input: grid = [
#         ["1","1","0","0","0"],
#         ["1","1","0","0","0"],
#         ["0","0","1","0","0"],
#         ["0","0","0","1","1"]
#       ]
#       Output: 3
# Constraints:
#       m == grid.length
#       n == grid[i].length
#       1 <= m, n <= 300
#       grid[i][j] is '0' or '1'.
##

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


# Problem
#     2D grid of numbers
#     1 represents land
#     0 represents water
#     If 1 is adjacent to zero (horiz or vert) shoreline
#     Find all islands (groupings of 1s surrounded by 0s)

# Observation
#     Diagonal is not a connection
#     If we search by complete row we will need to remember floats when searching next row
#     We could search a row and count the number of islands by toggling from land to water
#     Then when we start the next row we could count the number of islands and check for land above and below
#     This becomes algorithmically complex as we are constantly checking above below, toggling land booleans
#     Importantly it can be challenging as we are forced to consider reconnecting islands that were separate in previous rows

# Resources
#     Storing a row of values or conducting a row summation to extract information in mass could be useful
#         Values are strings and not summed easily
#         Hard to reconcile multiple island connections with lakes inbetween
#         Could conduct a lake search after
#         Every lake found, add back an island
#         This won't work lets consider other options
#     Activating a recursive search that checks all values on an island and writes them off from future searches
