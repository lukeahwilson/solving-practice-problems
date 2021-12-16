#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-16
# Question:
#       Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
#    sum and return its sum.
# Example:
#       Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#       Output: 6
#       Explanation: [4,-1,2,1] has the largest sum = 6.
# Constraints:
#       1 <= nums.length <= 105
#       -104 <= nums[i] <= 104
##


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        left_left = 0
        left_right = 0
        left_sum = nums[left_left]

        right_left = len(nums) - 1
        right_right = len(nums) - 1
        right_sum = nums[right_right]

        max_sum = max(left_sum, right_sum)

        while left_right < right_right:
            left_right += 1
            right_left -= 1

            if left_sum <= 0:
                left_left = left_right
                left_sum = 0

            if right_sum <= 0:
                right_right = right_left
                right_sum = 0

            left_sum += nums[left_right]
            right_sum += nums[right_left]

            if left_sum > max_sum or right_sum > max_sum:
                max_sum = max(left_sum, right_sum)

        return max_sum
        
# Problem
#     Given an array of integers
#     Return contiguous subarray with largest sum
#     Complete in O(n)

# Observation
#     Since numbers can be pos or neg, neg will hurt the total sum
#     So our goal is to remove neg numbers, unless larger pos nums exist
#     If we walk from left to right counting, or if right to left counting
#         if value goes negative, all preceeding values can be forgotten

# Resources
#     Input is in list format, can do len() and index return for O(1)

# Ideas
#     Can set a left pointer to left most, and start summing walking to the right
#         Check sum against a running max sum, replace max if the sum goes larger
#         If the sum goes negative, forget the sum, move pointer to new location
#         Store the indices for the new max that was found
#     Set a right pointer at right, sum walking inward, do the exact same from this side

# Concerns
#     When walking inward
#         are subsets getting forgotten about on either side?
#         are all possible subsets being checked or just one straddling the center?
#         do we need to repeat the search twice maybe

# Requirements
#     Two left pointers, one to store left boundary, one to walk rightward and check values
#         A left sum counting during the walk and comparing to max
#         A way to store the left sums pointers during the walk
#     Two right pointers, one to store right boundary, one to walk leftward and check values
#         A right sum counting and comparing to max
#         Storage for the right two pointers
#     End condition that returns at least a single value, this would happen when left right meet or cross
#         A way to make sure when they meet, they play nicely (imagining situations with 4 pointers all on one value)
#         When the end condition is met, need to know whether to return the lefts sum or right sum
#             Since it is simply a sum return (not an array return) we could just return max(left,right)

# Pseudocode
#     Initialize:
#         left left point (bound)
#         left right point (walks)
#         left sum
#         right left point (walks)
#         right right point (bound)
#         right sum
#         max sum (start at zero? start at single value?)

#     While left right hasnt crossed right_right
#         check if left sum went below zero
#             move bound inward
#             set left sum to zero to try again
#         check if right sum went below zero
#             move bound in
#             set right to zero
#         if one of the sums is larger than max sum
#             replace max sum
#         walk left pointer
#         walk right pointer
#         add val to left sum
#         add val to right sum
