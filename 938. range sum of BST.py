# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 
        self.res = 0
        self.inOrder(root, low, high)
        return self.res 
    
    def inOrder(self, root, low, high):
        if not root:
            return 
        if low <= root.val <= high:
            self.res += root.val 
        
        if high < root.val:
            self.inOrder(root.left, low, high)
        elif low > root.val:
            self.inOrder(root.right, low, high)
        else:
            self.inOrder(root.left, low, high)
            self.inOrder(root.right, low, high)
