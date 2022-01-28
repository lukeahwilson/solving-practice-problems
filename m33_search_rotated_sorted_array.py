#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-28
# Question:
#       There is an integer array nums sorted in ascending order with a rotation (with distinct values).
#   For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#   Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
#   or -1 if it is not in nums. You must write an algorithm with O(log n) runtime complexity.
# Example:
#       Input: nums = [4,5,6,7,0,1,2], target = 0
#       Output: 4
# Constraints:
#       1 <= nums.length <= 5000
#       -104 <= nums[i] <= 104
#       All values of nums are unique.
#       nums is an ascending array that is possibly rotated.
#       -104 <= target <= 104
##

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            center = (left + right) // 2
            if nums[center] < nums[0]: right = center - 1
            else: left = center + 1

        if nums[0] <= target: left = 0
        else: right = len(nums) - 1

        while left <= right:
            center = (left + right) // 2
            if nums[center] < target: left = center + 1
            elif nums[center] > target: right = center - 1
            else: return center
        return -1
