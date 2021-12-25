#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-24
# Question:
#       Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example:
#       Input: haystack = "hello", needle = "ll"
#       Output: 2
# Constraints:
#       0 <= haystack.length, needle.length <= 5 * 104
#       haystack and needle consist of only lower-case English characters.
##

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0

        h_length = len(haystack)
        n_length = len(needle)

        for h_index in range(h_length):
            if haystack[h_index:h_index+n_length] == needle:
                return h_index
        return -1
