#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-25
# Question:
#       You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
#       of the ith line are (i, 0) and (i, height[i]).
#       Find two lines that together with the x-axis form a container, such that the container contains the most water.
#       Return the maximum amount of water a container can store.
# Example:
#       Input: height = [1,8,6,2,5,4,8,3,7]
#       Output: 49
# Constraints:
#       n == height.length
#       2 <= n <= 105
#       0 <= height[i] <= 104
##

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_area = 0
        area = 0

        while right > left:
            print('Left', left)
            print('Right', right)

            area = min(height[right], height[left]) * (right - left)

            if max_area < area:
                max_area = area

            if height[right] < height[left]:
                right -= 1
            else:
                left += 1

            print('Height', min(height[right], height[left]))
            print('Width', (right - left))
            print('Area', area)
            print('Max', max_area)
            print()

        return max_area
