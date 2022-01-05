#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-05
# Question:
#       Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example:
#       Input: n = 3
#       Output: ["((()))","(()())","(())()","()(())","()()()"]
# Constraints:
#       1 <= n <= 8
##

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # Sol 1: Recursive DFS constructing only valid combos
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

        # Sol 2: Recursive BFS, inserting complete () and using sets to ignore invalid combos
        combos = ['']

        def get_combos(a, combos):
            new_combos = set()
            for combo in combos:
                for i in range(a):
                    new_combos.add(combo[:i] + '()' + combo[i:])
            return new_combos

        for a in range(1, n+1):
            combos = get_combos(a, combos)

        return combos
