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

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        print('Head Node', root.val)

        def compare (leftside, rightside):
            print('Left Node', leftside)
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
            return compare(leftside.left, rightside.right) and compare(leftside.right, rightside.left)

        return compare(root.left, root.right)
