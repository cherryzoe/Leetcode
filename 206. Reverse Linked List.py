# Reverse a singly linked list.

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # check if cur is None, is cur is None then get out the loop. 
        # Pre is at the tail of the original list, make pre as the head of reversed List and return new head.
        # Eg.
#         -----------------------
        # pre     cur      nex
        # None    head  -> a 
#         ------------------------
        #        pre      cur
        # None <- head    a  ->


        pre, cur = None, head       
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre
            
