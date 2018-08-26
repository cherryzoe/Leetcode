# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]

#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# Example 1:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# # Explanation: The LCA of nodes 2 and 8 is 6.
# Example 2:

# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself 
#              according to the LCA definition.
# Note:

# All of the nodes' values will be unique.
# p and q are different and both values will exist in the BST.

# 这道题我们可以用递归来求解，由于二叉搜索树的特点是左<根<右，所以根节点的值一直都是中间值，大于左子树的所有节点值，小于右子树的所有节点值，
# 那么我们可以做如下的判断，
# 如果根节点的值大于p和q之间的较大值，说明p和q都在左子树中，那么此时我们就进入根节点的左子节点继续递归
# 如果根节点小于p和q之间的较小值，说明p和q都在右子树中，那么此时我们就进入根节点的右子节点继续递归
# 如果都不是，则说明当前根节点就是最小共同父节点，直接返回即可

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
            
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        else:
            return root
