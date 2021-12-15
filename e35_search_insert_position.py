#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-15
# Question:
#       Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
#    return the index where it would be if it were inserted in order.
# Example:
#       Input: nums = [1,3,5,6], target = 7
#       Output: 4
# Constraints:
#       1 <= nums.length <= 104
#       -104 <= nums[i] <= 104
#       nums contains distinct values sorted in ascending order.
#       -104 <= target <= 104
##

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        upper = len(nums) - 1
        lower = 0
        look_here = 0

        while lower <= upper:
            look_here = (lower + upper) // 2
            if nums[look_here] == target:
                return look_here

            if nums[look_here] < target:
                lower = look_here + 1

            if nums[look_here] > target:
                upper = look_here - 1

        # This loop will always end with the upper bound crossing the lower bound
        # When the upper bound crosses the lower bound. The upper is equal to look_here
        # This means the value is meant to be in the location of the lower position

        return lower

# Problem
#     Given a sorted array, distinct integers, target val, return index of target
#     If no target val in array, return index it would be inserted
#     Write the alg with O(logn)

# Resources
#     Could use .index() to return index of target, but this is O(n) operation
#     Since array is already sorted, we could bisect list to eventually find location
#     len() is a O(1) operation

# Observations:
#     If we bisect the list, it might error if we have an empty list to bisect
#     If we return a new bisected list each time, we are running a O(n) operation
#     If we access an element in the list that is an O(1) operation
#     When we get to a single index, floor dividing that location could be weird
#     We will need to trigger the process to stop

# Idea:
#     We take len(array)//2
#     Check if accessed value is greater or smaller
#     than len(array)//2//2 and add or subtract to prev index
#     Check if accessed value is greater or smaller
#     Once we equalize, return the location (whether it is there or not)
#     we can keep the iteration floor dividing so long as the result is greater than 0

# Pseudocode:
#     set lookup location to length // 2
#     set lookup adjustment to lookup location // 2

#     while lookup adjustment // 2 > 0
#         check lookupvalue is greater target value
#             lookup location -= lookup adjustment

#         check if value is less than target value
#             lookup location += lookup adjustment

#         else return the lookuplocation
#         lookup adjustment //= 2

#     When loop ends, return the lookuplocation

# Challenges
#     Keeping track of the upper and lower bounds and not slipping by one at iterations will be a challenge
#     Every time I do an adjustment there is the potential to drop a value with my floor divide
#     Could implement some convoluted logic with modulus to save this value
#     Would be easier to take an upper and lower bound and reset each bound as needed

# Edge Cases
#     No values in the array (need to return 0 position)
#     Needs to be inserted in first position (need to return 0)
#     Needs to be inserted in last position (need to return last index +1 = length of array)
