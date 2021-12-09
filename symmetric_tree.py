#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-09
# Question:
#       Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Example:
#       Input: root = [1,2,2,3,4,4,3]
#       Output: true
# Constraints:
#       The number of nodes in the tree is in the range [1, 1000].
#       -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print('Head Node', root.val)
        return self.compare(root.left, root.right)

    def compare (self, leftside, rightside):
        print('\nLeft Node', leftside)
        print('Right Node', rightside)

        # If both the left and right side is null, they are mirrored, return True to previous recursive call
        if not leftside and not rightside:
            return True

        # If only one of the sides is null, they are not mirrored, return False to previous recursive call
        if not leftside or not rightside:
            return False

        # If the left side doesn't match the right side, it is not a mirrored condition
        if leftside.val != rightside.val:
            return False

        # Any single (or multiple) False sent backward recursively will propogate through and make the statement False
        # Recursively compare the left-tree's left and right-tree's right as well as left-tree's right with right-tree's left
        return self.compare(leftside.left, rightside.right) and self.compare(leftside.right, rightside.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        # Create a stack containing branches that can be iterated through
        stack = [[root.left, root.right]]

        # Iterate through the stack, continue until all branches have been explored (popped)
        while stack:
            print(stack[0][0])
            print(stack[0][1])
            print()
            # Create left and right variables equal to the last pair of branches in the stack
            left, right = stack[-1]
            # Now that we have set new branches to iterate through, remove these branches from the stack
            stack.pop()

            # If we've reached the end of the branches being compared, restart loop
            if not left and not right:
                continue

            # If either left or right but not both are null, then it isn't symmetrical
            if not left or not right:
                return False

            # If the values don't match, it isn't symmetrical
            if left.val != right.val:
                return False

            # Otherwise the values are the same, so append new branch pairs branching off of the checked left and right components
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])

        # If we iterate through all possible branches, comparing each node without returning a False, then the tree is symmetrical
        return True
