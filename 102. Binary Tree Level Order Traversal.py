Given a binary tree, return the level order traversal of its nodes' values. 
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]


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
    
    
