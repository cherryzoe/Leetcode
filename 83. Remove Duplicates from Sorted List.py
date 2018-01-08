# Given a sorted linked list, delete all duplicates such that each element appear only once.

# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.

# Idea:
# check if the value of cur.next is target value. If it is, then skip cur.next. cur point to cur.next.next. 
# Be noted that, once cur is re pointed to skip cur.next, it still needs to check is if the re pointed node 
# is the target node in the next round. Here we do NOT take additional step to move into next node!
# That is said, there are two cases: 
# 1. find the target node and skip it. Here we do NOT take additional step to move into next node!
# 2. not find and keep move on to next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
