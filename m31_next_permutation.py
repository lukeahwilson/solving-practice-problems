#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-26
# Question:
#       Given an array of integers nums, find the next lexicographically greater permutation of nums.
#       The replacement must be in place and use only constant extra memory.
# Example:
#       For example, the next permutation of arr = [1,2,3] is [1,3,2].
#       Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#       While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a larger rearrangement.
# Constraints:
#       1 <= nums.length <= 100
#       0 <= nums[i] <= 100
##

class Solution:
    '''
    1. Iterate from end (small sig digits) to start (big sig digits) to find smallest sig digit that decreases
    2. This represents the location where the smallest increase can be applied
    3. Next find the smallest bigger digit available in the previously iterated digits
    4. Now we swap these two digits to apply smallest increase at placeholder
    5. All following digits should be minimized by being sorted smallest to largest
    6. Since the following digits are ordered, they can simply be reversed
    7. If no possible change, reverse entire list
    '''
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                for j in range(i, len(nums)):
                    if j+1 == len(nums) or nums[j+1] <= nums[i-1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        nums[i:] = nums[:i-1:-1]
                        return
        nums[:] = nums[::-1]
