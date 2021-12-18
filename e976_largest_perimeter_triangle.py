#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-17
# Question:
#       Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
#   formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.
# Example:
#       Input: nums = [3,6,2,3]
#       Output: 8
# Constraints:
#       3 <= nums.length <= 104
#       1 <= nums[i] <= 106
##

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)[::-1]
        for index in range(len(nums)-2):
            if nums[index] < nums[index + 1] + nums[index + 2]:
                return sum(nums[index:index+3])
        return 0

# Challenge, can't just take the 3 largest values because if one is too large a triangle cannot be formed
# We either need to search the series twice, or we can conduct a sort first and then walk left to right
# Therefore we conduct a sort, walk left to right checking if the largest three values will make a triangle
