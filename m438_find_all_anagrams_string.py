#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-18
# Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/
##

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        left = 0
        right = len(p)
        anagram_locations = []

        for character in p:
            letter_count[character] -= 1
        for character in s[left:right]:
            letter_count[character] += 1

        if all(value == 0 for value in letter_count.values()):
            anagram_locations.append(left)

        while right <= len(s)-1:
            letter_count[s[left]] -= 1
            letter_count[s[right]] += 1
            left += 1
            right += 1

            if all(value == 0 for value in letter_count.values()):
                anagram_locations.append(left)

        return anagram_locations
