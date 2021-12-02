#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-11-29
# Question:
#       Given a string s, find the length of the longest substring without repeating characters.
# Example:
#       Input: s = "abcabcbb"
#       Output: 3
#       Explanation: The answer is "abc", with the length of 3.
# Constraints:
#       0 <= s.length <= 5 * 104
#       s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        substring = ''
        for character in s:

            if character in substring:
                substring = substring.split(character)[1]
            substring = substring + character

            if len(substring) > maxlength:
                maxlength = len(substring)

        return maxlength
