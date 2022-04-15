#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-14
# Question: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
##

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root

        queue = collections.deque([root])
        level = 0
        index = 0

        while queue:
            node = queue.popleft()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

			# This code is added to BFS to connect nodes
            index += 1
            if index < 2**level:
                node.next = queue[0]
            else:
                index = 0
                level += 1

        return root


# Since we are connecting nodes along levels horizontally, breadth first search is the obvious tool. This is a breadth first search algo:

# def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
# 	if not root: return root
# 	queue = collections.deque([root])
# 	while queue:
# 		node = queue.popleft()
# 		if node.left: queue.append(node.left)
# 		if node.right: queue.append(node.right)
# 		print(node)

# So now how do we connect the nodes from left to right?
# * Well queue[0] represents the next horizontal node. So node.next = queue[0] works.
# But we need to ensure we don't connect the end of one row to the start of the next
# * So use an index. When we hit the end of a row, reset the index and increase the row size by x2


#       Situation
# Given perfect binary tree = all leaves same level, numbers count upward, every parent 2 children
# Each node has a left, right, and next pointer

#       Problem
# Walk through the tree and update each node's next pointer with the node to the right

#       Notes
# Depth first search might push our pointers far away from adjacent nodes
# Perhaps breadth first search is more effective, stepping through the layers

#       Ideas
# Go to left node

#       What needs to happen
# Go to left node, set left.next = right
# Go to next level, left node next = right
# Go to right node, set right.next = node.next.left
# When no more nodes, go to right node, walk down
