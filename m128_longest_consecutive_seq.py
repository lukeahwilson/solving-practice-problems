#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-04
# Question:
#       Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Example:
#       Input: nums = [100,4,200,1,3,2]
#       Output: 4
#       Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Constraints:
#       0 <= nums.length <= 105
#       -109 <= nums[i] <= 109
##

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for num in nums:
            if num - 1 in num_set: continue
            seq_len = 1
            next_num = num + 1
            while next_num in num_set:
                seq_len += 1
                next_num += 1
            max_seq = max(max_seq, seq_len)

        return max_seq

#         Solution with dictionary:
#         nums_dict = {}
#         max_seq = 0

#         for num in nums:
#             if num - 1 in nums_dict:
#                 nums_dict[num] = nums_dict[num-1]
#             else:
#                 nums_dict[num] = num

#             next_num = num + 1
#             while next_num in nums_dict:
#                 nums_dict[next_num] = nums_dict[num]
#                 next_num += 1

#         for num in nums:
#             max_seq = max(max_seq, num + 1 - nums_dict[num])

#         return max_seq


# Problem:
# return the length of the longest consecutive elements sequence
# a consecutive element sequence is a sequence where each number increases by one
# the array is unsorted (Sorting is O(nlogn))
# the solution must run in O(n) (can't sort)


# Resources:
# Sort runs in O(nlogn), a sorted array would be easier to process
# Set has a O(1) lookup, store the matrix as a set for lookups
# Could do a set where all values are the same + 1
# union find could be an efficient method to reduce to only values that had a consecutive number


# Brute Force:
#     1. Take first value
#     2. Look in array for next value
#     3. Look in array for next value
#     4. Continue until no next number and save length
#     5. Repeat for next value


# Challenges:
# If I iterate through the matrix to store the array in a set, then run a loop checking the set I could complete in O(n^2)
# How can I compare all values to next values in one pass to avoid rerunning for each subsequent loop
# How do I eliminate any competing consecutive lengths?


# Questions to Self:
# Its one thing to take a minimum start thats known and iterate thru counting the consecutive numbers
# But how do we check for consecutive values that might start at a different value, eg. [100, 101, 102, 0, 1]
# This would require us to be tracking every single relationship between one number and the next


# Ideas:
# 1. Create two sets for array and array + 1
# Union, returns a set that contains the values that are in both but not the value at the beginning
# Run a while loop that ends when the union return is nothing, each loop adds 1 to length

# 2. Create dict for array
# walk through the array
# add number to the dictionary with:
#     - number as key
#     - value as itself
#     - if value -1 in dict, value = reference to number before in dictionary
#     - if value +1 in dict, key+1 value = reference to this number in dictionary
# at the end, walk the dictionary and check for the biggest difference in int value vs value for length


# Code Plan:

# Initialize a set for the array
# Initialize a set for the array + 1
# Run a union return on the sets to see all numbers that are consecutive to others

# [100,4,200,1,3,2,101]
# [101,5,201,2,4,3,102]
# [2,3,4,101]


# Pseudocode1:

# nums_set = set()
# nums_one = set()

# for num in nums:
#     add num to set
#     add num plus one to set

# cons_set = union()
# length = 0

# while cons_set:
#     length += 1
# return length

# Pseudocode2:

# nums_dict = {}

# for num in nums:
#     if num minus 1 is in dict, value = dict[num]
#     else value = int
#     if num plus 1 is in dict, dict[num plus 1] = dict[num]
#     dict[num] = value

# for num in nums:
#     max_seq = max(max_seq, num - dict[num])

# return max_seq
