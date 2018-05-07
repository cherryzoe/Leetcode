# Given a linked list, determine if it has a cycle in it.

# Follow up:
# Can you solve it without using extra space?

# solution 1: <need extra space but very fast>
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        st = set()
        p = head
        while p:
            if p in st:
                return True
            st.add(p)
            p = p.next
        return False
        

# solution 2:
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        fast, slow = head, head
        # while fast and fast.next: ==> 
        # 1. also good here, as long as to check two nodes not only one
        # 2. update on 5/7/18 Not working with error [1,2] no cycle, None type has no attribute 'next'
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
