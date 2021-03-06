# Given a singly linked list, determine if it is a palindrome.

# Follow up:
# Could you do it in O(n) time and O(1) space?

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = cur = head       
        pre = None
        
        # when fast reach the end of list, cur just reached the mid of the list
        # reverse the first half and then compare with the second half.
        while fast and fast.next:
            fast = fast.next.next # jump the fast pointer should perform before the reverse otherwise the nodes direction changes
            nex = cur.next 
            cur.next = pre
            pre = cur
            cur = nex
            
        # if the length of linked list is odd, then skip the middle node and start from mid+1
        # compare Node(mid+1) => Tail VS Head => Node(mid -1)    
        if fast:
            cur = cur.next
            
        while cur and pre and pre.val == cur.val:
        # it's critical to check cur is not reach the end (as None) every time loops a linked list. Otherwise None type of node does not have Value
            cur = cur.next
            pre = pre.next
        return not cur
