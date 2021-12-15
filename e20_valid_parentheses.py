#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-14
# Question:
#       Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', confirm the input string is valid.
# Example:
#       Input: s = "(]"
#       Output: false
# Constraints:
#       1 <= s.length <= 104
#       s consists of parentheses only '()[]{}'.
##

class Solution:
    def isValid(self, s: str) -> bool:
        square = 0
        bracket = 0
        paren = 0
        running = []

        for char in s:
            if char == '[':
                square += 1
                running.append('square')
            if char == '{':
                bracket += 1
                running.append('bracket')
            if char == '(':
                paren += 1
                running.append('paren')

            if char == ']':
                if running == [] or running.pop() != 'square':
                    return False
                square -= 1
            if char == '}':
                if running == [] or running.pop() != 'bracket':
                    return False
                bracket -= 1
            if char == ')':
                if running == [] or running.pop() != 'paren':
                    return False
                paren -= 1

            if square < 0 or bracket < 0 or paren < 0:
                return False

        if square == bracket == paren == 0:
            return True

        return False
