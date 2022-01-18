#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-17
# Question:
#       Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#   The overall run time complexity should be O(log (m+n)).
# Example:
#       Input: nums1 = [1,3], nums2 = [2]
#       Output: 2.00000
#       Explanation: merged array = [1,2,3] and median is 2.
# Constraints:
#       nums1.length == m
#       nums2.length == n
#       0 <= m <= 1000
#       0 <= n <= 1000
#       1 <= m + n <= 2000
#       -106 <= nums1[i], nums2[i] <= 106
##

# Need to write code to deal with repeating numbers getting dropped in set
# The plan before, binary searching for equilibrium and then returning was the wrong approach
# A left and right 2 pointer comparison would deal with edge cases better and be more elegant
# Although this solution seems at first fundamentally easy, it turns out it breaks under edge cases

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = sorted([nums1, nums2], key=len, reverse=True)

        length_1 = len(nums1)
        length_2 = len(nums2)
        length = len(nums1) + len(nums2)
        carry = (length + 1) % 2

        if not nums1 and not nums2: return None
        if not nums2 and carry: return sum(nums1[(length_1-1)//2:(length_1-1)//2+2])/2
        if not nums2:return nums1[(length_1-1)//2]

        median_1 = median_3 = median_5 = max(nums1)
        median_2 = median_4 = median_6 = max(nums2)
        locate_1 = (length - 1) // 2
        adjust = locate_1 // 2
        locate_2 = 0
        count = 0

        print('Nums1 =', nums1[locate_1:locate_1+1], 'At index', locate_1)
        print('Nums2 =', nums2[locate_2:locate_2+1], 'At index', locate_2)
        print('Adjust and Length', adjust)
        print('Carry', carry)
        print()

        while count < 2:
            if nums1[locate_1] < nums2[locate_2]:
                increment = min(adjust, length_1 - 1 - locate_1)
                locate_1 += increment # = min(length_1 - 1, locate_1 + increment)
                locate_2 -= increment # = max(0, locate_2 - increment)
            else:
                increment = min(adjust, length_2 - 1 - locate_2)
                locate_2 += increment # = min(length_2 - 1, locate_2 + increment)
                locate_1 -= increment # = max(0, locate_1 - increment)

            print('Nums1 =', nums1[locate_1], 'At index', locate_1)
            print('Nums2 =', nums2[locate_2], 'At index', locate_2)
            print('Adjust and Increment', adjust, increment)
            print()
            adjust //= 2
            if adjust == 0:
                median_1 = min(median_1, nums1[locate_1])
                median_2 = min(median_2, nums2[locate_2])
                median_3 = min(median_3, nums1[max(locate_1-1, 0)])
                median_4 = min(median_4, nums2[max(locate_2-1, 0)])
                median_5 = min(median_5, nums1[min(locate_1+1, length_1-1)])
                median_6 = min(median_6, nums2[min(locate_2+1, length_2-1)])
                print('Median_1 and Median_2', median_1, median_2)
                adjust += 1
                count += 1

        candidates_1 = set([median_1, median_3, median_5])
        candidates_2 = set([median_2, median_4, median_6])
        candidates = list(candidates_1) + list(candidates_2)
        candidates = sorted(candidates)
        locate = (len(candidates)-1) // 2
        if carry: median = sum(candidates[locate:locate+2])/2
        else: median = candidates[locate]

        print('Candidates', candidates)
        print('Median', median, '\n\n')

        return median
