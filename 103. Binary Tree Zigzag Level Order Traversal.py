Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

解题思路：
在101，102的基础上， 加上一个triiger判断即可
需要注意的是，一定是在读取value的时候再reverse，而不是存储Node的时候
若在将Node存入NexNode数组时reverse， 那么下次再遍历已反转的数组时，子节点的位置也会相应错乱。

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
        flag = 1
        
        while curNode:
            nexNode = []
            if flag == 1:
                res.append( [ node.val for node in curNode])
            else:
                res.append( [node.val for node in curNode[::-1]])
            flag = -flag
            for node in curNode:
                if node.left:
                    nexNode.append(node.left)
                if node.right:
                    nexNode.append(node.right)
            curNode = nexNode
        return res
