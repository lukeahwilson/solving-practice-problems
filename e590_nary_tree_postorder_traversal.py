#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-14
# Question: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
##

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        traversal = []

        def traverse(root):
            if not root:
                return

            for child in root.children:
                traverse(child)
                traversal.append(child.val)

        traverse(root)
        if root: traversal.append(root.val)

        return(traversal)
