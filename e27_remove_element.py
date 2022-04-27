#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-27
# Question: https://leetcode.com/problems/remove-element/
##

'''
1. Walk list in reverse [ O(n) ]
    2. If number is value: [ O(1) ]
        3a. Swap it with last number [ O(1) ]
        3b. Pop it from back of list [ O(1) ]
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for index in reversed(range(len(nums))):
            if val == nums[index]:
                nums[index], nums[-1] = nums[-1], nums[index]
                nums.pop()
