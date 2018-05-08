
# Given a linked list, swap every two adjacent nodes and return its head.

# Example:

# Given 1->2->3->4, you should return the list as 2->1->4->3.
# Note:

# Your algorithm should use only constant extra space.
# You may not modify the values in the list's nodes, only nodes itself may be changed.


# Solution:
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        pre.next = dummy.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, a.next, b.next = b, b.next, a
            pre = a
        return dummy.next
        
