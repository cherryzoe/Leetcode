# Remove all elements from a linked list of integers that have value val.

# Example
# Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# Return: 1 --> 2 --> 3 --> 4 --> 5

# Idea:
# cur point to head, loop through the list, if cur.next has the target val, skip cur.next and point to cur.next.next. 


Updated solution: 5/7/2018
        if not head:
            return
        dummy = pre = ListNode(0)
        dummy.next = cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
        
        
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        # this line - cur should be applied to head before the operation on head, why?
        cur = head
        # it must be while not if here for the case of [targetVal, targetVal, ....]
        while head and head.val == val:
            head = head.next
            
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            # Note: it must be else here. As for the case above, after we skip the target node, we should not move forward until we finish the next check if the value of             cur.next if the target value.
            # if the value of cur.next is the target value again, then we will keep skip the cur.next node while keep cur point to the same Node.
            else:
                cur = cur.next
            
        return head
                
