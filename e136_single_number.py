#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-24
# Question:
#       Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example:
#       Input: nums = [4,1,2,1,2]
#       Output: 4
# Constraints:
#       1 <= nums.length <= 3 * 104
#       -3 * 104 <= nums[i] <= 3 * 104
#       Each element in the array appears twice except for one element which appears only once.
##

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XoR Solution
        return reduce(lambda x, y: x^y, nums)
        # Math Solution
        return int(2*(sum(set(nums)) - sum(nums)/2))
