#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-17
# Question:
#       You are climbing a staircase. It takes n steps to reach the top.
#   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example:
#       Input: n = 3
#       Output: 3
#       Explanation: There are three ways to climb to the top.
#       1. 1 step + 1 step + 1 step
#       2. 1 step + 2 steps
#       3. 2 steps + 1 step
# Constraints:
#       1 <= n <= 45
##

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c, i = 1, 2, 3, 3
        while i < n:
            a = b
            b = c
            c = b + a
            i += 1
        if n < 3: return n
        return c

# Fibonacci Sequence
#         1

#         1 1
#         2

#         1 1 1
#         1 2
#         2 1

#         1 1 1 1
#         1 1 2
#         1 2 1
#         2 1 1
#         2 2

#         1 1 1 1 1
#         1 1 1 2
#         1 1 2 1
#         1 2 1 1
#         2 1 1 1
#         1 2 2
#         2 2 1
#         2 1 2

#         1 1 1 1 1 1
#         1 1 1 1 2
#         1 1 1 2 1
#         1 1 2 1 1
#         1 2 1 1 1
#         2 1 1 1 1
#         2 2 1 1
#         2 1 2 1
#         2 1 1 2
#         2 2 2
#         1 2 1 2
#         1 2 2 1
#         1 1 2 2
