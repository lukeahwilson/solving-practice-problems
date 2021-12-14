#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-13
# Question:
#       Given a roman numeral, convert it to an integer.
# Example:
#       Input: s = "MCMXCIV"
#       Output: 1994
#       Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# Constraints:
#       1 <= s.length <= 15
#       s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
#       It is guaranteed that s is a valid roman numeral in the range [1, 3999].
##

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev_char = 0
        romers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        for char in s:
            if romers[char] > prev_char:
                total -= prev_char
            else:
                total += prev_char
            prev_char = romers[char]

        total += prev_char
        return total

# Problem:
#     We will be given a string containing roman numerals
#     We need to convert the numerals to an integer

# Notes:
#     Each roman numeral is a multiplier that can be added towards a total
#     There isn't a place value system in numerals, meaning that we simply add
#     There is a chart defining numeral values
#     There are edge cases with sequences subtracting instead of adding

# Observations:
#     There being no place values, we can read left to right or vice versa, summing along the way
#     If a smaller numeral preceeds a larger numeral, it is subtracted, otherwise it's added

# Resources:
#     Can create a list of the numerals from smallest to largest
#     Can read string left to right, checking if the letter is larger or smaller than the next letter
#         - alternatively, we could code in every condition (i before v, i before x, x before..... etc)
#     If smaller we could subtract it, if larger we could add it
#     A hash table would be an effective way to tie a numeral to a value, and conduct a lookup

# Idea:
#     Create hash table of roman numerals
#     run a for loop on characters in the input string
#     check if the character is larger or smaller than the next character's lookup
#         - this will allow us to know if we need to subtract or add the number
#         - in order to do this, we'll need to run an indexed range to compare the two characters
#         - but now we need to consider how we deal with the last character
#     Alternatively, we compare against the previous character, and subtract or add the previous character
#         - this is done in a for char in string loop
#         - we set prevchar = char at end of each iteration
#         - we initialize prevchar as a zero on first loop
#         - thus the first loop will not add/sub anything, keeps it clean

# Pseudocode
#     romers = {I:1, ....}
#     total = 0
#     prev char = 0

#     for char in string:
#         if romers[char] > prev char:
#             subtract prev char from total
#         else:
#             add prev char to total
#         prev char = romers[char]

#     add the last prev char to the total
#     return total

# Edgecases:
#     No characters in string
#         - this is constrained, always at least one character
#     Only one character involved
#         - no problem, the prev_char = 0 gets added/subbed and makes no difference
#     All characters the same?
#         - Never triggers a subtraction, always adds previous character
