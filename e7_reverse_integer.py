#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-14
# Question:
#       Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
#       outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Example:
#       Input: x = -123
#       Output: -321
# Constraints:
#       -231 <= x <= 231 - 1
##

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0: value = str(x)[::-1].lstrip('0')
        if x < 0: value = '-' + str(x)[:0:-1].lstrip('0')
        if x == 0 or abs(int(value)) >= 2**31: return 0
        return value
