Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
解题思路：
快慢指针第一次相遇后，把快指针指回head。俩指针同步走，第二次相遇点必然是入口。
详细证明 - https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        # 如果链表中没有环，那么slow与fast不会相遇。 出while循环是否因为fast走到无环表尾部
        if not fast or not fast.next:
            return

        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next 
        return fast
