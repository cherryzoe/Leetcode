# Write a program to find the node at which the intersection of two singly linked lists begins.

# For example, the following two linked lists:

# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗            
# B:     b1 → b2 → b3
# begin to intersect at node c1.

# Notes:

# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.

consider following test cases:
1. L1 and L2 have difference lenght but intersection occurs => can find intersection after switch head
2. L1 and L2 have samelenght and intersection occurs => can find intersection before switch head
3. No intersection => reach the tail in first loop(if length equal) or second loop ( different length) and return None

Updated version 5/7/2018
       
         if not headA or not headB:
            return None
        
        pA, pB = headA, headB
        while pA != pB:
            if not pA:
                pA = headB
            else:
                pA = pA.next
                
            if not pB:
                pB = headA
            else:
                pB = pB.next                                 
        return pA
        
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
       
        pa, pb = headA, headB
        
        while pa is not pb:
            pa = pa.next
            pb = pb.next
            
            if pa == pb:
                 return pa   
                 #in case of when pa and pb reach the end of linked list: pa = None and pb = None, return None. 
            if pa is None:
                pa = headB
            if pb is None:
                pb = headA
                
        return pa
