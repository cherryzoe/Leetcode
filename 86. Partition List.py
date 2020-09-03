Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

解题思路：
分别新建两个链表，List1存放比x小的值，List2存放大于等于X的值，最后将L2接到L1末尾，组成一个链表。
注意此题需要dummy node,也需要手动将第二个链表结尾指向None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next 
            else:
                l2.next = head
                l2 = l2.next 
            head = head.next 
        l1.next = h2.next
        l2.next = None
        return h1.next 
