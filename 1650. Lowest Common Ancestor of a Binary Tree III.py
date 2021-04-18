"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        root = p
        # find the root of the tree, the rest will be same with LCA solution
        while root.parent:
            root = root.parent
        return self.traverse(root, p, q)

    def traverse(self, root, p, q):
        if not root:
            return root

        if root.val == p.val:
            return root 

        if root.val == q.val:
            return root
        
        l = self.traverse(root.left, p, q)
        r = self.traverse(root.right, p, q)

        if l and r:
            return root
        return l or r
        


     
