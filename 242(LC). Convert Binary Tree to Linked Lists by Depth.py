# 242. Convert Binary Tree to Linked Lists by Depth
# 中文English
# Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).

# 样例
# Example 1:

# Input: {1,2,3,4}
# Output: [1->null,2->3->null,4->null]
# Explanation: 
#         1
#        / \
#       2   3
#      /
#     4
# Example 2:

# Input: {1,#,2,3}
# Output: [1->null,2->null,3->null]
# Explanation: 
#     1
#      \
#       2
#      /
#     3

class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
            
        curLevel = collections.deque([root])
        res = []
        
        head, tail = ListNode(0), None
        
        while curLevel:
            head.next = None
            tail = head
            
            nexLevel = []
            
            for node in curLevel:
                tail.next = ListNode(node.val)
                tail = tail.next
            res.append(head.next)
            
            for node in curLevel:
                if node.left:
                    nexLevel.append(node.left)
                if node.right:
                    nexLevel.append(node.right)
                
            curLevel = nexLevel
            
        return res
