Reverse a singly linked list.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, cur = None, head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        head = pre
        return head
            
