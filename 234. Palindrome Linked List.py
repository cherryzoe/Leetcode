Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = cur = head       
        pre = None
        
        while fast and fast.next:
            fast = fast.next.next
            nex = cur.next 
            cur.next = pre
            pre = cur
            cur = nex
            
        if fast:
            cur = cur.next
            
        while cur and pre and pre.val == cur.val:
            cur = cur.next
            pre = pre.next
        return not cur
