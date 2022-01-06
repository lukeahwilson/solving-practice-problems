#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-01-05
# Question:
#       Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example:
#       Input: head = [1,2,3,4,5]
#       Output: [5,4,3,2,1]
# Constraints:
#       The number of nodes in the list is the range [0, 5000].
#       -5000 <= Node.val <= 5000
##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], past = None) -> Optional[ListNode]:
    # Recursive
        if head:
            temp = head
            head = head.next
            temp.next = past
            past = temp
            return Solution.reverseList(self, head, past)
        return past

    # Iterative
        past = None
        while head:
            temp = head
            head = head.next
            temp.next = past
            past = temp
        return past

#     [1,2,3,4,5] Head = 1, Next [2,]
#     [2,3,4,5]   Head = 2, Next [3,]
#     [3,4,5]     Head = 3, Next [4,]
#     [4,5]       Head = 4, Next [5,]
#     [5]         Head = 5, Next []

#     [5]         Head = 5, Next [4,3,2,1,None]
