# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

8/7/2020
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                # in case l1 is not valid Node and through out exception
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry = v1 + v2 + carry
            # cur.next.val = carry % 10
            cur.next = ListNode(carry % 10)
            carry /= 10
            cur = cur.next
            v1 = v2 = 0
        return dummy.next

--------
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = l = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            summ, carry = carry, 0
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
            if summ > 9:
                carry = summ / 10
                summ = summ % 10
            l.next = ListNode(summ)
            l = l.next
        return dummy.next
        
