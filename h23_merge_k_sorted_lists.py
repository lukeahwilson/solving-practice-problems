#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-17
# Question: https://leetcode.com/problems/merge-k-sorted-lists/
##

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = sorter = ListNode()

        nodes = dict()

        for index in range(len(lists)):
            if lists[index]:
                nodes[index] = lists[index]

        while nodes:
            min_value = float("inf")
            for index, node in nodes.items():
                if node.val < min_value:
                    min_value = node.val
                    min_index = index

            sorter.next = nodes[min_index]
            sorter = sorter.next

            if nodes[min_index].next:
                nodes[min_index] = nodes[min_index].next
            else:
                nodes.pop(min_index)

        return sorted_list.next
