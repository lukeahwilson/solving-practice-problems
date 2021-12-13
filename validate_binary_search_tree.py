#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-13
# Question:
#       Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# Example:
#       Input: root = [5,1,4,null,null,3,6]
#       Output: false
#       Explanation: The root node's value is 5 but its right child's value is 4.
# Constraints:
#       The number of nodes in the tree is in the range [1, 104].
#       -231 <= Node.val <= 231 - 1
##

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        left_limit = float(-inf)
        right_limit = float(inf)

        def check(root, left_limit, right_limit):

            # Check that we have not reached the end of a branch, this is how we end the recursive loop
            if root is None:
                # print('Node is Null')
                return True

            # print('\nTree', root)
            # print('Left_limit', left_limit)
            # print('Parent Node', root.val)
            # print('Right_limit', right_limit)

            # A valid tree must only have nodes greater in value in it's right branch and lesser in it's left
            # So when checking a node value, we confirm it is greater than a min allowable, and less than a max allowable
            if not root.val > left_limit or not root.val < right_limit:
                return False

            # print('Right_Limit < Val < Left_Limit')

            # We run recursion here, tunneling down until we reach our node is null ending where we return true
            # The recursion, reinserts nodes as the leftward and rightward values each time, requestion 2 recursions for the binary tree
            # When walking to the right, the node will need to be greater than the value immediately before, but less than the lowest historic limit
            # When walking to the left, the node will need to be less than the value immediately before, but greater than the greatest historic limit
            # We achieve this in recursion with the following: return (walk right/update min/maintain max) and (walk left/update max/maintain min)
            return check(root.right, root.val, right_limit) and check(root.left, left_limit, root.val)

        # Now we call the recursive function to initiate the recursion. We need to start with limits set to pos/neg infinity
        # Pos/Neg infinity gives room for the branches to walk as deep in either direction as necessary
        return check(root, left_limit, right_limit)
