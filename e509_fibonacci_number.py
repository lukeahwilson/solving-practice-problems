#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-06
# Question:
#       Given n, calculate F(n).
# Example:
#       Input: n = 4
#       Output: 3
#       Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
# Constraints:
#       0 <= n <= 30
##

class Solution:
    def fib(self, n: int, total = 0, previous = 1, i = 0) -> int:
        # Dynamic Programming
        if i >= n: return total
        temp = total
        total = total + previous
        previous = temp
        return Solution.fib(self, n, total, previous, i + 1)

        # Recursive Call
        # if n <= 1: return n
        # return Solution.fib(self, n-1) + Solution.fib(self, n-2)

        # Math Cheat
        # return int((((1 + 5 ** 0.5) / 2) ** n + 1) / 5 ** 0.5)
