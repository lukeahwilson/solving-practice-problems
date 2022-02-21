#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-02-21
# Question:
#       Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path
#   such that adding up all the values along the path equals targetSum. A leaf is a node with no children.
# Example:
#       Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#       Output: true
#       Explanation: The root-to-leaf path with the target sum is shown.
# Constraints:
#       The number of nodes in the tree is in the range [0, 5000].
#       -1000 <= Node.val <= 1000
#       -1000 <= targetSum <= 1000
##

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return
        if not root.left and not root.right and root.val == targetSum: return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# Start by checking if we've searched to the end of a branch and return False if we have
# Check ahead to see if we are on a leafe (no root.left or root.right) and if the root.val equals the remaining targetSum
# Do an OR search to either side to search left and right for sums and return the TRUE by leveraging OR to preserve True
