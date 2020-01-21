# Given a binary tree, return the level order traversal of its nodes' values. 
# (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# 解题思路：
# -   用一个数组存放当current level 的 Node, 首先得到其所有节点的值。然后判断每个节点是否有子节点, 若有则放到nex中
# -   需要注意的是 nex 数组在每次循环开始时初始化为空
# -   比较容易疏忽的是返回时存Node的val而不是Node

1/21/2010
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root:
            return []
        res = []
        queue = collections.deque([root])
        
        while queue:
            res.append([node.val for node in queue])
            lenq = len(queue) #it's critical to get length as a variable, otherwise the length of queue would be dynamicly change while adding more nodes into it
            for _ in range(lenq):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res

# solution1 - iterative, time complex: O(n) Space complex : O(1)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        cur = [root]
        res = []
        
        while cur:
            res.append( [ node.val for node in cur ] )
            nex = []
            for node in cur:
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            cur = nex
        
        return res
    
 
# solution 2 - recursive,  time complex: O(n) Space complex : O(n)
#  用level记录当前层数，level每增加一层，res的长度增加1. 当层数>res的长度时，往res中增加一个新空集用于后续记录该层的节点
#     res = [[nodes.val in level 0], [nodes.val in level1], ...]

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []
        self.helper(root, 0, res)
        return res
    
    def helper(self, node, level, res):
        if not node:
            return 
        if level >= len(res):
            res.append([]) 
        res[level].append(node.val)
        self.helper(node.left, level + 1, res)
        self.helper(node.right, level + 1, res)
