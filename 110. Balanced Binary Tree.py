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
solution 1： O(N)
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

#  求二叉树是否平衡，根据题目中的定义，高度平衡二叉树是每一个节点的两个字数的深度差不能超过1，
# 那么我们肯定需要一个求各个点深度的函数，然后对每个节点的两个子树来比较深度差，时间复杂度为O(NlgN)
# 但不是很高效，因为每一个点都会被上面的点计算深度时访问一次，我们可以进行优化。方法是如果我们发现子树不平衡，
# 则不计算具体的深度，而是直接返回-1。那么优化后的方法为：对于每一个节点，我们通过checkDepth方法递归获得左右子树的深度，
# 如果子树是平衡的，则返回真实的深度，若不平衡，直接返回-1，此方法时间复杂度O(N)，空间复杂度O(H)，见方法1

Solution2 O(NlgN)：
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
