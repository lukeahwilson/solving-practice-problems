#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-20
# Question:
#       You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0
#   represents water.
# Example:
#       Input: grid = [[1,0]]
#       Output: 4
# Constraints:
#       row == grid.length
#       col == grid[i].length
#       1 <= row, col <= 100
#       grid[i][j] is 0 or 1.
#       There is exactly one island in grid.
##

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = range(len(grid))
        cols = range(len(grid[0]))
        perim = 0

        for i in rows:
            for j in cols:
                neighbours = 0
                if grid[i][j]:
                    if i-1 in rows and grid[i-1][j]:
                        neighbours += 1
                    if j-1 in cols and grid[i][j-1]:
                        neighbours += 1
                    if i+1 in rows and grid[i+1][j]:
                        neighbours += 1
                    if j+1 in cols and grid[i][j+1]:
                        neighbours += 1
                    perim += 4 - neighbours

        return perim
