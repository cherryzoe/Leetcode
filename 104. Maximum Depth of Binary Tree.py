Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        depth = 0
        stack = [root]
        while stack:
            nxLevel = []
            for node in stack: 
                if node.right:
                    nxLevel.append(node.right)
                if node.left:
                    nxLevel.append(node.left)         
            stack = nxLevel
            depth += 1
        return depth