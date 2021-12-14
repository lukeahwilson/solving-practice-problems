#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-11-30
# Question:
#       An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome.
# Example:
#       Input: x = 121
#       Output: true
# Constraints:
#       -231 <= x <= 231 - 1

class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = str(x)
        middle = len(digits) // 2
        bisect = (len(digits) + 1) % 2
        return(digits[(middle-bisect)::-1] == digits[middle:])
