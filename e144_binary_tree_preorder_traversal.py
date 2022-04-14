#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-14
# Question: https://leetcode.com/problems/binary-tree-preorder-traversal/
##

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        def traverse(root):
            if not root:
                return

            traversal.append(root.val)
            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return traversal