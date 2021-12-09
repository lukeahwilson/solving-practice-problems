#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-09
# Question:
#       Given the root of a binary tree, return its maximum depth.
# Example:
#       Input: root = [3,9,20,null,null,15,7]
#       Output: 3
# Constraints:
#       The number of nodes in the tree is in the range [0, 104].
#       -100 <= Node.val <= 100

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         return max(self.depth_search(root, 0, []))

#     def depth_search(self, root, depth, depths):

#         depths.append(depth)

#         if root:
#             depth += 1
#             self.depth_search(root.left, depth, depths)
#             self.depth_search(root.right, depth, depths)

#         else:
#             depth -= 1

#         return depths
