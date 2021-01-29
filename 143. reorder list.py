给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

解题思路：
1. 通过快慢指针找到中点， 如果总长度是偶数，慢指针停在后半段第一个，奇数则是中间一点。这两种情况最后都是一样的，不需要特殊处理
2. 把后半段逆转
3. 前后交叉指，形成最终结果

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # h1->1->2-None   None <-3<-4<- slow
        if not head:
            return []

        fast, slow = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next 
        
        pre = None 
        while slow:
            nex = slow.next
            slow.next = pre
            pre = slow
            slow = nex 

        mid = pre
        h = head
        while h and mid:
            nex1 = h.next
            nex2 = mid.next
            h.next = mid
            mid.next = nex1
            h = nex1
            mid = nex2
        return head
     
