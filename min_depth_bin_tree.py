#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-13
# Question:
#       Given an array of integers nums and an integer target,return indices of the two numbers such that they add up
#    to the target. Can you come up with an algorithm that is less than O(n2) time complexity?
# Example:
#       Input: nums = [2,7,11,15], target = 9
#       Output: [0,1]
#       Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Constraints:
#       2 <= nums.length <= 104
#       -109 <= nums[i] <= 109
#       -109 <= target <= 109
#       Only one valid answer exists.
##

# Problem:
#     Given a binary tree, find the length of the shortest leaf node (node with no children)
#     Root node to on node below only, would be a total length of 2

# Observations:
#     We don't need to be returning information at every single level, (no recursive number tracking necessary?)
#     We need to be able to return a minimum value at a given depth in our search
#     This could either be done by returning a value, checking it remains minimum, and subsequently returning it
#     Or it could be done by setting an internal attribute (min_path) and then checking on each pass and replacing if right

# Resources:
#     We can use internal left/right methods to drive the tree one step along each direction
#     With recursion, we could return a value that gets tracked and updated with +1 , -1, at each step
#     or we could simply return zero + 1 at each level and take the minimum from left and right trees (easier for stepping)

# Plan:
#     Start a recursive depth search with a function find_shortest_path
#     Check that there is a node, otherwise return zero
#     Check if the min_path is now smaller and update
#         - Problem, if we check if it is smaller and update along the way, how do we build the first minimum path?
#         - Perhaps we don't set an attribute to zero at the beginning, instead we return a minimum all the way to the top
#     Return min(leftside, rightside) + 1

# Edge Cases:
#     No leafs
#         - Returning left right with pull 0,0 and add 1 for one node
#     No tree
#         - Root is none and will instantly return 0
#     One branch
#         - Problem, code takes no leaf as being the shortest distance
#         - Need if statement, confirming that there is at least one leaf long

# Pseudocode:
#     if root none return zero (edge case for no root in first place)
#     function (root)
#         initialize left and right to max values so they're irrelevant until a return
#         if left and right leafs are none return 1
#         if left leaf exists run recursive loop down left
#         if right leaf exists run recursive loop down right
#         return the minimum of the left and right options
#     return function(root)

class Solution:
    # Recursive Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def find_shortest_path(root):
            left, right = float(inf), float(inf)

            if root.left is None and root.right is None:
                return 1

            if root.left:
                left = find_shortest_path(root.left)

            if root.right:
                right = find_shortest_path(root.right)

            return min(left, right) + 1

        return find_shortest_path(root)

    # Iterative Breadth 1st Search Method
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [[root, 1]]

        while stack:
            root, depth = stack.pop(0)
            if root.left is None and root.right is None:
                return depth
            if root.left:
                stack.append([root.left, depth + 1])
            if root.right:
                stack.append([root.right, depth + 1])
