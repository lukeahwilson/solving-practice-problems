#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-14
# Question:
#       Given a binary tree, determine if it is height-balanced.
#       (a binary tree in which the left and right subtrees of every node differ in height by no more than 1)
# Example:
#       Input: root = [3,9,20,null,null,15,7]
#       Output: true
# Constraints:
#       The number of nodes in the tree is in the range [0, 5000].
#       -104 <= Node.val <= 104
##

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Create attribute of whether the tree is balanced
        self.balanced = True

        # Run recursive function to search tree with depth-first search
        def check_balance (root):
            # When we reach the end of the tree, we return 0, terminating the recursion
            if root is None:
                return 0

            # At each node, run a recursive search down the left and right branches
            left, right = check_balance(root.left), check_balance(root.right)

            # Check that the left and right branches are balanced per criteria
            if abs(left - right) > 1:
                # Using this attribute, we can set balance to False from deep in the recursive loop
                self.balanced = False

            # If root not None, and tree is balanced, we return max of left and right + 1.
            # Essentially, once 0 is triggered at branch end, node above records 0 + 1 and returns
            # Next the node above that will take max of left / right and return that + 1
            # The recursive loops add 1 at each level until the parent node is reached
            return max(left, right) + 1

        check_balance(root)
        return self.balanced

# PROCESS (Struggled with this one):

        # PROBLEM
        # Balanced tree is a tree where any branch in one direction, will have a branch the other way of equal or plus/minus 1 depth
        # Every branch, we need to check the depth at the left and at the right
        ## Each node, check if it's a node (not null) and then check left and check right

        # RESOURCES
        # Since we have a tree, with linkages in its class definition, we can put its internal left/right methods to work if we want
        # Left method and right method, returns the node at the left and right

        # OBSERVATIONS
        # The order of the input is node, node.left, node.right, node.left.left, node.left.right, node.right.right

        # MATH IDEA
        ## Perhaps some complex math alg could apply 2^n starting with n=0 and adding n when nodes are called
        ## To conduct a search along the array confirming there is equal depth
        ## Every single split would require connectivity to the correct subsequent nodes. This seems very complex

        # RECURSIVE
        ## We can run recursion using by returning the function we right, while inputing .left and .right
        ## The recursive loop tunnels down until no node is found and it is then returned True
        ## In order to track a value along the recursive tunnel, we need to reinsert a value into the function

        # PSEUDOCODE
        ## def check_balance(root, tree_height, current_height):
        ##     confirm root value is not null (return true if it is to end loop)
        ##
        ##         compare our heights of our left right branches
        ##         we know our height once we've reached the end of the tree
        ##         we've reached the end of the tree when the node becomes null
        ##     so we check if node is null and if it is we set a tree height
        ##
        ##     if we haven't reached the end of the tree, we continue adding to the height
        ##         height is height plus 1
        ##         perhaps we just reinsert into the recursion, current_height + 1
        ##
        ##     check that the height is not different
        ##         if the current height is different
        ##         and the node is null (tree height is established)
        ##         return false
        ##
        ##        return check_balance(root.left, tree_height, current_height+1) and check_balance(root.right, tree_height, current_height+1)
        ##
        ##    check_balance(root, 0, 0)

        # 1st Draft Code
        ## def check_balanced (root, tree_height, current_height):
        ##
        ##     if root.val is None:
        ##         return current_height
        ##         return True
        ##
        ##     if root.val is not None:
        ##         curr = curr + 1
        ##
        ##     if root.val is None and abs(current_height-tree_height) > 0
        ##         return False
        ##
        ##     return check_balance(root.left, tree_height, current_height+1) and check_balance(root.right, tree_height, current_height+1)
        ##    check_balance(root, 0, 0)

        # 2nd Draft Code
        ## def check_balance (root, current_height):
        ##     if root.val is None:
        ##         return current_height - 1
        ##
        ##     return abs(check_balance(root.left, current_height+1)-check_balance(root.right, current_height+1)) <= 1
        ##
        ## return check_balance(root, 0)

        # 3rd Draft Code
        ## def check_balance (root, current_height):
        ##     if root is None:
        ##         return 0
        ##
        ##     print()
        ##     print(root)
        ##     print(current_height)
        ##     print(check_balance(root.left, current_height+1) - check_balance(root.right, current_height+1))
        ##
        ##     if root.left is None and root.right is None:
        ##         # print(current_height)
        ##         return current_height - 1
        ##
        ##     return abs(check_balance(root.left, current_height+1)-check_balance(root.right, current_height+1)) <= 1
        ##
        ## return check_balance(root, 0)

        ## Challenge
        ## I did not structure my loop to return maximums and instead have it returning the local value each time
        ## I can tunnel True/False from deeper returns, but I can't just tunnel integer returns upward, these are replaced
        ## I need to find a way to search for a maximum, and subsequently during the recursion check left against right
        ## Note that if we are choosing to return a maximum, then we are not returning a boolean
        ## We can either return both the maximum and the boolean to make this work, or toggle an attribute in the class
        ## Toggling an attribute is much easier. Make sure to check if we should toggle before returning max.
