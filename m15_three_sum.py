#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-29
# Question:
#       Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
#   and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.
# Example:
#       Input: nums = [-1,0,1,2,-1,-4]
#       Output: [[-1,-1,2],[-1,0,1]]
# Constraints:
#       0 <= nums.length <= 3000
#       -105 <= nums[i] <= 105
##

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)
        triplets = dict()
        options = set()
        zerocount = 0
        answer = []
        key = 0

        for number in nums:
            options.add(number)
            if number == 0: zerocount += 1

        if zerocount >= 3:
            answer += [[0, 0, 0]]

        for index1 in range(length):
            target1 = 0 - nums[index1]

            for index2 in range(length):
                target2 = target1 - nums[index2]

                if target2 in options \
                    and index1 != index2 \
                    and target2 != nums[index1] \
                    and target2 != nums[index2]:

                    if {target2, nums[index1], nums[index2]} in triplets.values():
                        continue

                    triplets[key] = {target2, nums[index1], nums[index2]}
                    answer += [[target2, nums[index1], nums[index2]]]
                    key += 1

        return answer
