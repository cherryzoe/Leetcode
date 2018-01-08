# Find the nth to last element of a singly linked list. 

# The minimum number of nodes in list is n.

# Have you met this question in a real interview? Yes
# Example
# Given a List  3->2->1->5->null and n = 2, return node  whose value is 1.
   
# Idea:
# Used two pointer fast and slow. Make fast move N steps and then slow begins move at the same pace. 
# while fast reaches the end of list, slow should stop at the position len(list) - n, which is the desired result.
   
   def nthToLast(self, head, n):
        # write your code here
        if head is None:
            return None
        fast = slow = head
        while n>0:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
                
# Solution 2:
#    Idea: find out the length of the list. then move length - n + 1 steps
     
   def nthToLast(self, head, n):
        # write your code here
        cur = head
        le = 0
        
        if head is None:
            return None
        # be noted: check cur.next instead of cur. Otherwise le would be greater (one plus) the actual size
        while cur.next:
            le += 1
            cur = cur.next
        cnt = le - n + 1
        while cnt and head:
            head = head.next
            cnt -= 1
        return head
