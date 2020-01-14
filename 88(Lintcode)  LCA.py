
# 88. Lowest Common Ancestor of a Binary Tree
# 中文English
# Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

# The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

# Example
# Example 1:

# Input：{1},1,1
# Output：1
# Explanation：
#  For the following binary tree（only one node）:
#          1
#  LCA(1,1) = 1
# Example 2:

# Input：{4,3,7,#,#,5,6},3,5
# Output：4
# Explanation：
#  For the following binary tree:

#       4
#      / \
#     3   7
#        / \
#       5   6
			
#  LCA(3, 5) = 4
# Notice
# Assume two nodes are exist in tree



# 这道题目和Lowest Common Ancestor of a Binary Search Tree
# 类似，只不过现在条件变为一颗普通的二叉树，要求出最低公共祖先。

# 首先要先确定给的两个node是否都在tree里，如果都在tree里的话，就可以分成3种情况，第一种情况是两个节点是在公共祖先的左右两侧，
# 第二种情况是都在树的左侧，第三种情况是都在树的右侧，如果是第二，第三种情况的话，公共祖先就在给定的两个点中比较上面的那一个。

# 如果转换成代码的话，从上往下走，base case分为3种，判断遇到了p就直接返回p，遇到q就直接返回q，不用向下做了。
# 如果left,right都不为空，就返回root自己；left,right哪一个不为空就返回哪个，整个recursion做完就可以得到LCA。

# 这道题的解法关键在于要想清楚两点：
# 1. 如果p 和q同时出现在了两侧，那么这个节点就一定是LCA
# 2. 如果p 和q中只有一个出现在了某一侧，那么出现了的那个就是LCA

# 这个题里面lowestCommonAncestor(root, p, q)函数的作用是判断p和q在root树中最低的公共祖先是什么，返回值是公共祖先。

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        
        if not root:
            return 
        if root == A:
            return root
        if root == B:
            return root
            
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left and right:
            return root
        else:
            return right or left
