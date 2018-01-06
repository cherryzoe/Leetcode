Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        curNode = [root]
        
        while curNode:
            res.append( [ node.val for node in curNode ] )
            nexNode = []
            for node in curNode:
                if node.left:
                    nexNode.append(node.left)
                if node.right:
                    nexNode.append(node.right)
            curNode = nexNode
            
        return res[::-1]
