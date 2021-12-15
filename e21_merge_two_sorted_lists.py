#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-15
# Question:
#       You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list.
#    The list should be made by splicing together the nodes of the first two lists.
# Example:
#       Input: list1 = [1,2,4], list2 = [1,3,4]
#       Output: [1,1,2,3,4,4]
# Constraints:
#       The number of nodes in both lists is in the range [0, 50].
#       -100 <= Node.val <= 100
#       Both list1 and list2 are sorted in non-decreasing order.
##


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return output.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Problem
#     Given two sorted and linked lists
#     Need to merge the two lists into one sorted list
#     The returned list should be made by splicing the nodes of the first two lists

# Resources
#     Linked lists have built in method val which returns the node value
#     and .next which returns the attached following list respectively

# Observations
#     Each list can have any number of nodes and length
#     Lists have integer values at nodes
#     We traverse a list with node = node.next, read a value with node.val, and read the linked list from node with node

# Ideas
#     We can add a node at the end of the list, by traversing to the end (while node.next, node = node.next) then node.next = Node(value)
#     We can insert a node at the beginning of the list with list = Node(value), list.next = oldlist.next
#     We can insert a node mid way with insertnode = Node(value), insertnode.next = list.next, list.next = insertnode.next

# Plan
#     Compare the two list node values
#     If list2node smaller or same, insert infront
#         and we shift list2 node to node.next
#     if larger, wait
#         and we shift list1 node to node.next
#     if list1 is fully traversed
#         add remaining list2 nodes to list1 node.next and return
#     if list2 gets fully traversed
#         return

# Simpler Plan
#     Start a separate linked list (rather than in place)
#     If list1node smaller or same, set the node value to list1 and shift list1 to next
#     Else we take list2 node and shift it to next
#     When fully traversed append
