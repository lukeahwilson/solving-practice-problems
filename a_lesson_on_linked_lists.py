#!/usr/bin/python
# PROGRAMMER: Luke Wilson
# DATE CREATED: 2022-04-15
##


# Reversing a Linked List
'''
1. We need to track the past and thus need a past variable
2. We need to iterate thru the list and thus use our head variable
3. We need somewhere to store information as we switch pointers, thus hold
a. The past starts pointing at None (Null)
b. We iterate through the linked list with 'while head' and 'head = head.next'
c. We need to maintain the old head position to create a past history
d. Now that we've moved the head to the next position, lets aim our hold backward
Note. if we do this before head = head.next, it will change both pointers and destroy the list
e. Now lets increment our past to include the previous head pointing backward
f. At completion, we return the past as it represents the reversed list
    a.  while head
    b.      hold = head, this needs to happen first before we change the head
    c.      head = head.next
    d.      hold.next = past,
    e.      past = hold
    f.  return past

Recursive solution is the same, instead of a while loop, we iterate head and past recursively
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Solution
        past = None
        while head:
            hold = head
            head = head.next
            hold.next = past
            past = hold
        return past

        # Recursive Solution
        def reverse_it(head, past):
            if not head: return past
            hold = head
            head = head.next
            hold.next = past
            past = hold
            return reverse_it(head, past)
        return reverse_it(head, None)



# Detecting a cycle in a linked list
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Iterative Solution
        while head:
            if head.val == 'Visited': return True
            head.val = 'Visited'
            head = head.next
        return False

        # Recursive Solution
        if head:
            if head.val == 'Visited': return True
            head.val = 'Visited'
            return self.hasCycle(head.next)
        return False



# Sorting 2 linked lists
'''
Similar to reversing a linked list, but our intermediary needs to create a sorted path between lists
1. initialize the sorted_list, similar to the past variable for reversing linked list
2. initialize the sorter that will move along the chain, similar to the temp variable
3. while there are nodes in the two lists, we iterate along comparing node values
4. make the sorter, and by extension the sorted_list point towards the lower value number
5. update the list that was chosen to be at the next location on the chain
6. update the sorter to be in the next position to sort the next number
7. once complete we add remaining nodes to the end of the sorter
8. the sorted_list was sorted by the sorter incrementing along
9. return sorted_list.next, as the first node was an empty intitializer
'''
# Iterative approach
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sorted_list = sorter = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                sorter.next = list1
                list1 = list1.next
            else:
                sorter.next = list2
                list2 = list2.next
            sorter = sorter.next

        if list1:
            sorter.next = list1
        if list2:
            sorter.next = list2
        return sorted_list.next

# Recursive Solution
# Beautifully tunnels down to bottom in order of values
# Once it reaches end, it returns the values in order
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2



# Removing the nth node from the end of a linked list
# 1. Two Pointer Method, Initialize Follower and Leader
# Give leader a lead equal to the offset n
# Move pointers together once lead reached
# Skip the followers next node once the leader reaches the end
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fixed = follower = ListNode()
        fixed.next = follower.next = leader = head
        lead = 0

        while leader:
            lead += 1
            leader = leader.next
            if lead > n:
                follower = follower.next
# NOTE IMPORTANT NOTE, below changes original fixed list directly which is the goal
# This is because we are moving through the nodes, and then suddenly resetting one of the nodes
# If we destroy a connection in the linkage, we need to manually reconnect and reset it!
        follower.next = follower.next.next
        return fixed.next

# Arithmetic Method
# retrieve the length of the list, this can be done with below recursive tunnel
# subtract n from the length to obtain the remove index
# if first node needs to be removed, return node.next
# otherwise we walk forward until our index reaches the remove index
# here we remove the next node using node.next = node.next.next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length(head, length):
            if head: return get_length(head.next, length + 1)
            return length
        remove_index = get_length(head, 0) - n

        if remove_index == 0: return head.next
        index = 1

        node = head
        while node and index < remove_index:
            index += 1
            node = node.next
        node.next = node.next.next
        return head
