# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Idea:
#   - compare each node and merge into the new linked list
#   - be noted that we need to create a dummy node because as the end of merge we lose the new head. So dummy would be the best way to store the head and return.
  
  class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0) 
        # cur is pointed to head, that means cur.next = newHead, dummy.next = newHead
        
        while l1 and l2:
            if l1.val < l2.val: 
            # as to linked list, compare the value of node, not the node itself.
                cur.next = l1 
                l1 = l1.next   
                # if l1 reaches the end of list, l1 = None, it will be out of the while loop in the next iteration
            else:
                cur.next = l2
                l2 = l2.next   
                # if l1 reaches the end of list, l1 = None, it will be out of the while loop in the next iteration
            cur = cur.next
        cur.next = l1 or l2
        
        return dummy.next
        
