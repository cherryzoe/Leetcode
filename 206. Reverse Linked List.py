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
            
# solution2 recursive:
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head, None)
    
    def helper(self, head, newHead):
        if not head:
            return newHead
        nextNode = head.next
        head.next = newHead
        return self.helper(nextNode, head)
or
# he recursive version is slightly trickier and the key is to work backwards. 
# Assume that the rest of the list had already been reversed, now how do I reverse the front part? 
# Let's assume the list is: n1 → … → nk-1 → nk → nk+1 → … → nm → Ø

# Assume from node nk+1 to nm had been reversed and you are at node nk.

# n1 → … → nk-1 → nk → nk+1 ← … ← nm

# We want nk+1’s next node to point to nk.

# So,

# nk.next.next = nk;

# Be very careful that n1's next must point to Ø. If you forget about this, your linked list has a cycle in it. 
# This bug could be caught if you test your code with a linked list of size 2.
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
