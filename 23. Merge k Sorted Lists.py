# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        minHeap = []
        dummy = ListNode(0)
        head = dummy
        # 取各个链表的头节点，存入最小堆。按照元组第一个元素大小排序 - node.val
        for node in lists:
            if node:
                heapq.heappush(minHeap, (node.val, node))
        
        while minHeap:
            val, node = heapq.heappop(minHeap)
            head.next = node
            head = head.next 
            if node.next:
                heapq.heappush(minHeap, (node.next.val, node.next))
        return dummy.next

    
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        dummy = ListNode(0)
        cur = dummy
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize():
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return dummy.next
        
        
        
 from operator import attrgetter

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None
