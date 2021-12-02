#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-11-27
# Question:
#       Given an array of integers nums and an integer target,return indices of the two numbers such that they add up
#    to the target. Can you come up with an algorithm that is less than O(n2) time complexity?
# Example:
#       Input: nums = [2,7,11,15], target = 9
#       Output: [0,1]
#       Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Constraints:
#       2 <= nums.length <= 104
#       -109 <= nums[i] <= 109
#       -109 <= target <= 109
#       Only one valid answer exists.

class Solution:
    # O(n) Solution due to O(1) lookup table replacing second search
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_lookup = {}
        for idx in range(len(nums)):
            missing_value = target - nums[idx]
            if missing_value in dict_lookup:
                return [dict_lookup[missing_value], idx]
            dict_lookup[nums[idx]] = idx

    # O(n^2) Solution due to double loops
        # a = 0
        # b = 0
        # for x in nums:
        #     for y in nums:
        #         if x + y == target and a != b:
        #             return [a, b]
        #         b += 1
        #     b = 0
        #     a += 1
