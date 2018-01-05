# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.

解题思路
- 一般BST的问题，首先往divide & conquer的思路去想
- 一棵二叉树是不是平衡二叉树 => 左子树是不是平衡二叉树？右子树是不是平衡二叉树？
- 如果任意一颗子树不平衡，整个树肯定不平衡
- 如果左右子树都是平衡的，但左右子树相差高度大于1，此刻这课树又是不平衡的
- 问题转化为分别对左右子树求maxDepth，平衡就返回最大深度，不平衡就返回-1
- 技巧：用-1表示它不是一颗平衡二叉树


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.maxDepth(root) != -1
        
    def maxDepth(self, root):
        if not root:
            return 0       
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
