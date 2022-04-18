#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-17
# Question: https://leetcode.com/problems/reverse-string-ii/
##

class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        start = 0
        end = k -1
        transformed = s[end::-1]
        print(transformed)

        while start < len(s):
            start += k
            end += k
            transformed += s[start:end+1]
            print(transformed)
            start += k
            end += k
            transformed += s[end:start-1:-1]
            print(transformed)

        return transformed

#     Situation
# given a string s, s is greater than 0
# an integer k, k is greater than 0
# doesnt indicate if output or if occurs in place. will assume output

#     Problem
# 1. reverse the first k characters for every 2k characters
#     -that is reverse the first k characters
#     -then dont reverse next k characters
#     -then reverse the following 2k characters
# 2. if the number of characters left doesn't match the total left to operate on, complete operation
#     - POSSIBLE EDGE CASE

#     Observations
# given a string, would be nice to switch characters in place to save memory
# append a piece of reverse string using string[start:end:-1] (Counts backwards, start > end I should double check this syntax)

#     Ideation
# we could start at index 0, count forward by k times, append this piece of string to a new transformed string
# then we could increment start and end by k, then append this piece of string to the new transformed string
#     -this should be O(n) time complexity which is good
#     -this requires a second string resulting in O(n) memory which could be improved if we operate in place
#     -let's proceed with this solution as it gives a good foundation to convert to inplace later if time

#     Edge Cases:
# what if k is zero? algo won't increment. Do we leave as is? k must be greater than 0.
