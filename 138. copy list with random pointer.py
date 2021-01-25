
解题思路：
用两次遍历原链表，同时用哈希表存老节点：新节点的映射
比如老节点7，新建一个节点，值为7，但是新节点的内存地址完全与老节点无关。这就是为什么要等节点被创建之后，才可以分配指针指向他。
第一次遍历，新建节点，仅存node.val ==》这一步很重要，因为这就相当于新建了一个Node所以我们就有了这个节点，并且有了节点的地址。这样第二遍才可以指向已知节点的地址。
第二次遍历，把next random信息补上，其实就是指向哪个Node

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None 
        # 哈希表存储 key=老节点，value=新节点
        visted = {}
        dummy = head
        # 第一次遍历，建立新节点
        while dummy:
            newHead = Node(dummy.val, None, None)
            visted[dummy] = newHead
            dummy = dummy.next      
        # 第二次遍历,把next和random信息填上
        dummy = head
        while dummy:
            if dummy.next:
                visted[dummy].next = visted[dummy.next]
            if dummy.random:
                visted[dummy].random = visted[dummy.random]
            dummy = dummy.next
        # 返回的是哈希表中的映射，而不是直接返回newHead
        return visted[head]
