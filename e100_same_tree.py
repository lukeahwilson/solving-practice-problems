#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-08
# Question:
#       Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#       Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
# Example:
#       Input: p = [1,2,3], q = [1,2,3]
#       Output: true
# Constraints:
#       The number of nodes in both trees is in the range [0, 100].
#       -104 <= Node.val <= 104

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both nodes are null
        # If the end of the branch was reached, then both nodes will be null and we can return True
        if not p and not q:
            return True

        # If both nodes are not null, then we check if the nodes are different from one another
        # If the nodes are different, or one is null, then we return False
        if not p or not q or p.val != q.val:
            return False

        print(p.val, q.val)

        # Now we recursively drive through the branches, checking all left options and all right options at each pass
        # Each time, pass, the values must be the same or else we return False.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
