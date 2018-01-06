# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

解题思路：
在#101，#102的基础上， 一行隔一行反转。 加上一个triiger判断是否需要反转即可。
需要注意：
    1.  一定是在读取value的时候再reverse，而不是存储Node的时候
    若在将Node存入NexNode数组时reverse， 那么下次再遍历已反转的数组时，子节点的位置也会相应错乱。
    2. 此解法将trigger变量初始化为1， 之后可用trigger = - trigger
    如果用boolean, 之后用 trigger = not trigger 即可

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        curNode = [root]
        trigger = 1
        
        while curNode:
            nexNode = []
            # 判断是够需要反转此level的节点
            if trigger == 1:
                res.append( [ node.val for node in curNode])
            else:
                res.append( [node.val for node in curNode[::-1]])
            trigger = -trigger
            for node in curNode:
                if node.left:
                    nexNode.append(node.left)
                if node.right:
                    nexNode.append(node.right)
            curNode = nexNode
        return res
