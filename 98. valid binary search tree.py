
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1

解题思路：
判断是否是binary search tree，需要满足左子树所有节点都小于root，右子树所有节点都大于root，当涉及到所有节点时，需用递归。
由于二叉搜索树的以上性质，用中序遍历所有节点值得到的数组应该是递增、非递减的
这里建一个全局变量数组，中序遍历的递归时，往数组中存入节点值

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = []

        if not root:
            return True
        self.inorder(root)
        for i in range(len(self.res)-1):
            if self.res[i+1] <= self.res[i]:
                return False
        return True

    def inorder(self, root):
        if not root:
            return 
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
