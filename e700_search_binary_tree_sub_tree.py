#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-14
# Question: https://leetcode.com/problems/search-in-a-binary-search-tree/
##
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val: return root
        if root.val > val: return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)

# since a binary tree is ordered by values, we can tunnel down only the path of lower values and return None elsewhere
# once we arrive at the value, we can return that value back up through the tunnel


# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         traversal = []

#         def build_subtree(root):

#             if not root:
#                 return
#             if root.left:
#                 traversal.append(root.left.val)
#             if root.right:
#                 traversal.append(root.right.val)
#             build_subtree(root.left)
#             build_subtree(root.right)

#         def traverse(root):
#             if not root:
#                 return
#             if root.val == val:
#                 traversal.append(root.val)
#                 build_subtree(root)
#                 return
#             traverse(root.left)
#             traverse(root.right)

#         traverse(root)

#         return traversal
