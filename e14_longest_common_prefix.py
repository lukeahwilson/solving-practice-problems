#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-13
# Question:
#       Write a function to find the longest common prefix string amongst an array of strings.
# Example:
#       Input: strs = ["flower","flow","flight"]
#       Output: "fl"
# Constraints:
#       1 <= strs.length <= 200
#       0 <= strs[i].length <= 200
#       strs[i] consists of only lower-case English letters.
##

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        prefix = ''
        minlength = float(inf)

        for string in strs:
            minlength = min(minlength, len(string))

        while index < minlength:

            character = strs[0][index]

            for string in strs:
                if string[index] is not character:
                    return prefix
            prefix += character
            index += 1

        return prefix
        
# problem:
#     given a list of strings
#     compare prefixes in each string (starting letters)
#     find the longest common prefix among all of the strings

# observations:
#     since all of the individual strings must have the prefix
#         - we don't need to compare each to every other
#         - we can instead check that all still have it and count

# resources:
#     for string in list of strings we can check first character
#     count up, once a character doesn't match, exit the loop
#     return the count

# edgecases:


# pseudocode:
#     prefix is empty
#     index is zero
#     matching is True

#     while matching is True:
#         iterate index
#         for string in string_list:
#             if string[index] then character is string[index]
#             else return prefix
#             if string[index] is not character return prefix
#         add character to prefix

#     return prefix
