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

解题思路：
-   用一个数组存放当current level 的 Node, 首先得到其所有节点的值。然后判断每个节点是否有子节点, 若有则放到nex中
-   需要注意的是 nex 数组在每次循环开始时初始化为空
-   比较容易疏忽的是返回时存Node的val而不是Node



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
    
    
