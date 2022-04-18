#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-17
# Question: https://www.hackerrank.com/challenges/tree-top-view/problem
##

"""
ATTEMPTED TO SOLVE FOR ALL UNDERLING BRANCHES
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):

    #Write your code here
    top_view = []
    if not root: return top_view

    def dfs_inorder(node, position, left):
        if not node: return

        dfs_inorder(node.left, position + 1, max(right, position))
        dfs_inorder(node.right, min(position - 1, -1))
        if position >= left:
            top_view.append(node.info)

    def dfs_preorder_rightward(node, position, right):
        if not node: return
        if position >= right:
            top_view.append(node.info)

        dfs_preorder_rightward(node.right, position + 1, max(right, position))
        dfs_preorder_rightward(node.left, min(position - 1), max(right, position))


    dfs_inorder(root, 0, 0)
    dfs_preorder_rightward(root.right, 0, 0)
    print(*top_view)
