#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-01
# Question:
#       Given a string s, return the longest palindromic substring in s.
# Example:
#       Input: s = "babad"
#       Output: "bab"
#       Note: "aba" is also a valid answer.
# Constraints:
#       1 <= s.length <= 1000
#       s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n^2) Solution:
        maxpalindrome = ''
        center = 0
        index = 0

        # O(n)
        while index <= len(s)*2:        # Need to check all letters and between all letters
            bisect = index % 2          # A bisect is added to shift to between letters using modulus
            center = index // 2         # Repeat the operation with the bisect at each index
            palindrome = 1 + bisect     # If on letter, 1, if between letters, start at 2
            offset = 0                  # Initialize offset

            print('\ns[', center + bisect / 2, ']', s[center:center + bisect + 1])

            # Iterate outwards toward left and right while the following statements are true:
                # The left side of our search stops by the beginning of the string
                # The right side of our search stops before the ending of the string
                # The leftmost and rightmost character is the same (the right side is offset plus bisect)

            # O(n)
            while (center - offset) >= 0 and (center + offset + bisect) <= len(s)-1 and s[center - offset] == s[center + offset + bisect]:

                print('s[', center - offset, ':', center + offset + bisect + 1,']', s[center - offset : center + offset + bisect + 1])
                print('Palindrome Length =', palindrome, 'Max Length =', len(maxpalindrome))

                # If the palindrome is larger than the max recorded palindrome, use the indices to capture the new max palindrome
                if palindrome > len(maxpalindrome):
                    maxpalindrome = s[center - offset : center + offset + bisect + 1]
                    print('NEW MAX PALINDROME', maxpalindrome)

                # Iterate the offset by 1, add 2 to the palindrome length since we build in both directions
                offset += 1
                palindrome += 2

            index += 1
        return maxpalindrome


        # # O(n^3) Solution
        # maxlength = ''
        # index = 0
        # # Check characters from left to right
        # for char in s: # O(n)
        #     string = ''
        #     # Build substring out from left to right
        #     for subchar in s[index:]: # O(n)
        #         string += subchar
        #         # Read substring left to right and compare to its reverse
        #         if string[:] == string[::-1]: # O(n)
        #             palindrome = string
        #         if len(palindrome) > len(maxlength):
        #             maxlength = palindrome
        #     index += 1
        # return maxlength
        # # A lot of reused computation that looks very similar to eachother
        # # Is it possible to combine some of these generated insights into a single iteration?
