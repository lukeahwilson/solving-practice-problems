#!/usr/bin/python
# PROGRAMMER: Luke Wilson
##

"""
Dynamic Programming Examples (Great for checking number of ways something creates something)
"""
# Process of storing information to avoid repeating work.
# Bottom Up Dynamic Programming Fibonacci
class Solution:
    def fib_bottom_up_iterative(n):
        if n <= 1: return n
        small = 0
        large = 1
        total = 0
        for i in range(n-1):
            total = small + large
            small = large
            large = total
        return total

# Bottom Up Dynamic Programming Generate Parenthesis
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combos = ['']

        def get_combos(a, combos):
            new_combos = set()
            for combo in combos:
                for i in range(a):
                    new_combos.add(combo[:i] + '()' + combo[i:])
            return new_combos

        for a in range(1, n+1):
            combos = get_combos(a, combos)
            print(combos)

            combos = []

# Another example would be, find the sets of numbers that add up to x when given an array.
# Dynamic Programming, would skip repeating every single addition at every level.
    # instead, we could build combos. by creating a dictionary connecting an index to a tuple (value, contributing numbers)
    # then we cyclically go back to this dictionary, adding a number to combos below it.
    # once we go larger than the target we stop
    # any values equal to the target get their contributing numbers added to it

"""
Backtracking Example:
"""
# Backtracking is a general algorithm for finding all (or some) solutions to some computational problems.
# The idea is that it incrementally builds candidates to the solutions, and abandons a candidate ("backtrack")
# as soon as it determines that this candidate cannot lead to a final solution.

# Implementing Backtracking to Generate Parenthesis
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combos = []

        def build_combos(left_count, right_count, constructor):
            if left_count < n:
                build_combos(left_count+1, right_count, constructor+'(')

            if left_count > right_count:
                build_combos(left_count, right_count+1, constructor+')')

            if left_count == right_count == n:
                combos.append(constructor)

        build_combos(0, 0, '')
        return combos

# Backtracking to determine what
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                # make a deep copy of the current combination
                results.append(list(comb))
                return
            elif remain < 0:
                # exceed the scope, stop exploration.
                return

            for i in range(start, len(candidates)):
                # add the number into the combination
                comb.append(candidates[i])
                # give the current number another chance, rather than moving on
                backtrack(remain - candidates[i], comb, i)
                # backtrack, remove the number from the combination
                comb.pop()

        backtrack(target, [], 0)

        return results


"""
Divide and Conquer Example
"""




"""
Sliding Window Examples
"""
# Length of Longest Substring
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

# Find All Anagrams in a String (Sliding Window with Counter, initialize alphabet and check first set of characters)
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

# Length of Longest Palindrome (Expand around Center)
 class Solution: # O(n^2) Solution:
    def longestPalindrome(self, s: str) -> str:
        maxpalindrome = ''
        center = 0
        index = 0

        while index <= len(s)*2:        # Need to check all letters and between all letters
            bisect = index % 2          # A bisect is added to shift to between letters using modulus
            center = index // 2         # Repeat the operation with the bisect at each index
            palindrome = 1 + bisect     # If on letter, 1, if between letters, start at 2
            offset = 0                  # Initialize offset

                # Iterate outwards toward left and right while the following statements are true:
                # The left side of our search stops by the beginning of the string
                # The right side of our search stops before the ending of the string
                # The leftmost and rightmost character is the same (the right side is offset plus bisect)

            while (center - offset) >= 0 and (center + offset + bisect) <= len(s)-1 and s[center - offset] == s[center + offset + bisect]:
                # If the palindrome is larger than the max recorded palindrome, use the indices to capture the new max palindrome
                if palindrome > len(maxpalindrome):
                    maxpalindrome = s[center - offset : center + offset + bisect + 1]
                # Iterate the offset by 1, add 2 to the palindrome length since we build in both directions
                offset += 1
                palindrome += 2

            index += 1
        return maxpalindrome



"""
Two Pointer Examples (Also Used for Binary Search)
"""
# Two Sum Problem Example

# O(n) Solution due to O(1) lookup table replacing second search
        num_lookup = dict()
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in num_lookup:
                return [num_lookup[compliment], i]
            num_lookup[nums[i]] = i

# O(nlog(n)) Solution and O(n) memory using sort and dictionary to track indices
        index = 0
        for num in nums:
            nums[index] = (num, index)
            index += 1

        nums = sorted(nums)

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1], nums[right][1]]
            if nums[left][0] + nums[right][0] > target:
                right -= 1
            if nums[left][0] + nums[right][0] < target:
                left += 1
        return
