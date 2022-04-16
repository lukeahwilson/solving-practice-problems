#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-15
# Question: https://leetcode.com/problems/swap-nodes-in-pairs/
##

'''
Below is a more plainly written equally fast solution even if it's a few more lines. Simple put:
    - Use four pointers offset by one from eachother: left_left, center_left, center_right, right_right
    - Every second cycle we swap the center left and center right pointers, the outsides are used to reset connections
    - At the end of each cycle we move all our pointers to the right once
    - NOTE: A left_left pointer is necessary to reconnect the head to the swapped list, otherwise it just gets cut up
'''
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head                   # Confirm list is of swappable length

        head = ListNode(0, head)                                    # Start head at one location earlier
        left_left = head                                            # We have 4 variables,
        center_left = left_left.next                                # the left most (left_left) relinks the head
        center_right = center_left.next                             # the center_left and center_right get swapped
        right_right = center_right.next                             # the right most gives reference for the swapping

        swap = 0                                                    # we initialize a swap value and cycle it on and off
        while center_right:                                         # until the center right finishs, we keep swapping
            swap = (swap + 1) % 2                                   # this cycles swap on and off
            if swap:                                                # every second cycle we swap
                center_left.next = right_right                      # point center left past center right directly at right most
                center_right.next = center_left                     # point center right to center left
                temp = center_left                                  # use a temp to reset center left and center right
                center_left = center_right                          # reset center left
                center_right = temp                                 # reset center right
                left_left.next = center_left                        # left most points at center_left and we've completed the swap

            if right_right: right_right = right_right.next          # move right right pointer (will go out of bounds on last node so we have condition)
            center_right = center_right.next                        # move center right pointer
            center_left = center_left.next                          # move center left pointer
            left_left = left_left.next                              # move left left pointer

        return head.next                                            # return the head.next for the swapped linked list


#   Situation
# One lists given with values (values might count upward but it doesn't clarify in the instruction)

#   Problem
# Need to swap every second node, for example odd positions moved upward to even positions, and even backward to odd

#   Constraints
# Not allowed to change node values to do this swap (that wouldn't really be a swap afterall)

#   Edge Case Thoughts
# No nodes in list
# One node in list
# Odd number of nodes

#   Possible Resources
# Keep a counter and check that it is even or odd, or have it cycle on off, could do by +1 // 2

#   Observations
# Similar to a reverse a linked list in some sense as we'll need to keep a temp or hold and use it to send pointers in different directions

#   Ideas
# Reverse list structure
#   Create a swapped list = head
#   Create a swapper node = head
#   Use a swap_cycle by floor dividing by 2 and counting by 1

#   Simplify First
# How do we reverse two nodes?
# past = None
# hold = head
# while head:
#   head = head.next
#   hold = head
#   hold.next = past
#   past = hold
#

#   Plan
# Walk along the list forward:
#   Step forward one
# If swap is on make swap
