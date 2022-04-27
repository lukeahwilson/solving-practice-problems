#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-27
# Question: https://leetcode.com/problems/sqrtx/
##

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        num = str(x)
        right = int('1' + num[int(len(num)/2):])

        while left <= right:
            root = int((left + right)/2)
            if root*root > x: right = root - 1
            elif root*root < x: left = root + 1
            else: return root
        return int((left + right)/2)
