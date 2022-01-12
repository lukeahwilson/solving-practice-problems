#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-12
# Question:
#       Given n non-negative integers representing an elevation map where the width of each bar is 1,
#   compute how much water it can trap after raining.
# Example:
#       Input: height = [4,2,0,3,2,5]
#       Output: 9
# Constraints:
#       n == height.length
#       1 <= n <= 2 * 104
#       0 <= height[i] <= 105
##

class Solution:
    def trap(self, height: List[int]) -> int:
        peak = height.index(max(height))
        water = 0
        level = 0
        for i in range(0, peak):
            level = max(level, height[i])
            water += level - height[i]

        level = 0
        for i in range(len(height)-1, peak, -1):
            level = max(level, height[i])
            water += level - height[i]

        return water
