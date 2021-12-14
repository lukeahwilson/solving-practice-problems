#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2021-11-28
# Question:
#       You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
#    reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a
#    linked list.
# Example:
#       Input: l1 = [2,4,3], l2 = [5,6,4]
#       Output: [7,0,8]
#       Explanation: 342 + 465 = 807.
# Constraints:
#       The number of nodes in each linked list is in the range [1, 100].
#       0 <= Node.val <= 9
#       It is guaranteed that the list represents a number that does not have leading zeros.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = 0
        multiplier = 1
        # print(l1)
        while l1 is not None:
            answer += multiplier*l1.val
            multiplier *= 10
            l1 = l1.next
        # print(l1)

        multiplier = 1
        while l2 is not None:
            answer += multiplier*l2.val
            multiplier *= 10
            l2 = l2.next

        output = node = ListNode(0)
        for number in reversed(str(answer)):
            node.next = ListNode(number)
            # print(node)
            node = node.next
            # print(node)

        # while output is not None:
        #     print(output.val)
        #     print(output)
        #     output = output.next

        return output.next
