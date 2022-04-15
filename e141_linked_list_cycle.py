#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-15
# Question: https://leetcode.com/problems/linked-list-cycle/
##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 'Visited': return True
            head.val = 'Visited'
            head = head.next
        return False

        if head:
            if head.val == 'Visited': return True
            head.val = 'Visited'
            return self.hasCycle(head.next)
        return False



#       Problem
# Given a linked list, looking for a node that is reached again by contiously following next, creating a loop
# Return True if a cycle exists, otherwise return false

#       Plan
# Lets start by iterating through the linked list
# We will need to track if we have visited a node yet

#         Challenge
# how do we track if a node was visited?
# if we use the node value, duplicate values would break this

# Ideas
# store a new linked list next pointer at each location pointing at something random
    # (doesn't work, can't keep it attached, memory intensive too)

# store a history of nodes visits? how do we avoid duplicate node values?
#   this could possibly be solved by creating an array of values, and looking for a duplicate array to be created
#       what if there are repeat patterns tho? This breaks above solution

# can we change the value to a unique identifier? theoretically this could break if a node happened to have the same value
# I'm assuming that head.val = 'Visited' is a satisfactory solution, in practice I'd use a unique proof value
