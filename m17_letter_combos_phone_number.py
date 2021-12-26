#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-26
# Question:
#       Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
#   number could represent. Return the answer in any order.
# Example:
#       Input: digits = "23"
#       Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Constraints:
#       0 <= digits.length <= 4
#       digits[i] is a digit in the range ['2', '9'].
##

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Return empty list if no digits provided
        if not digits: return []
        assignments = {'2':['a', 'b', 'c'],
                        '3':['d', 'e', 'f'],
                        '4':['g', 'h', 'i'],
                        '5':['j', 'k', 'l'],
                        '6':['m', 'n', 'o'],
                        '7':['p', 'q', 'r', 's'],
                        '8':['t', 'u', 'v'],
                        '9':['w', 'x', 'y', 'z']}

        # Need to create a function that will recursively build out a tree of options as new digits are provided
        def add_combos(combos, number):
            new_combos = set()                      # Create empty set of combinations
            for combo in combos:                    # Iterate thru all made combos up until this number
                for letter in assignments[number]:  # Iterate thru all letters corresponding to the number added
                    new_combos.add(combo + letter)  # Add each possible letter for this number to all current combos
            return new_combos                       # Return the new and extended list of combos


        combos = ['']                               # Start combos off with '' so that it iterates once thru as empty
        for number in digits:                       # For each number in the provided digits, run the add_combos alg
            combos = add_combos(combos, number)     # Recursively set combos to new combos with old combos and next number
        return combos                               # Once all digits have been ran, return the final list of combos
