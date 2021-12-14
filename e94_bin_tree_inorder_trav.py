#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-08
# Question:
#       Given the root of a binary tree, return the inorder traversal of its nodes' values.
# Example:
#       Input: root = [1,null,2,3]
#       Output: [1,3,2]
# Constraints:
#       The number of nodes in the tree is in the range [0, 100].
#       -100 <= Node.val <= 100

# Testcase [1,2,3,4,5,null,6,7,null,8,null,9,10,11,null,12,13,null,14,null,null,null,null,15,null,null,null,null,null,16]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Return inorder traversal of it's node values
        # Inorder traversal, means running left operation first, than visiting node, than running right
        # Observe that the search drives down first leftmost branch, than searches, and after expiring, recursively drives down next branches
        # There is no call back to the previous node, the recursive search simply dies, and subsequent nest recursive searches continue
        # For example, once all recursive leftward searches die, the starting node will then toggle to next line of code to begin right branch

        traversal = []

        def traverse(tree, depth):
            print('Tree Depth = ', depth)
            print('Traversal =', traversal)

            if tree:
                depth += 1
                print('Node Value =', tree.val)
                print('\nTraverse Left')
                traverse(tree.left, depth)

                print('\nBranch End, Return to Parent (', tree.val,')')
                print('Read Node Value', tree.val,'to Traversal')
                print('Tree Depth =', depth-1)
                traversal.append(tree.val)

                print('\nTraverse Right')
                traverse(tree.right, depth)
            else:
                print('Node is Null')
                depth -= 1

        traverse(root, 0)
        return traversal
