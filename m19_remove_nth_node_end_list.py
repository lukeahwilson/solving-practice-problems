#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-12-29
# Question:
#       Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Example:
#       Input: head = [1,2,3,4,5], n = 2
#       Output: [1,2,3,5]
# Constraints:
#       The number of nodes in the list is sz.
#       1 <= sz <= 30
#       0 <= Node.val <= 100
#       1 <= n <= sz
##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def get_length(head, length):
            if head: return get_length(head.next, length + 1)
            return length

        remove_index = get_length(head, 0) - n

        if remove_index == 0: return head.next

        def remove_node(head, remove_index, index):
            node = head
            while node and index < remove_index:
                index += 1
                node = node.next
            node.next = node.next.next
            return head

        head = remove_node(head, remove_index, 1)
        return head
