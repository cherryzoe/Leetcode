Given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them.

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

  
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

解题思路：BST的特点是通过中序遍历之后得到的数组一定单调递增。
1. 中序遍历输入的树，得到数组
2. 取数组中点作为根节点，分割成左右两边子树，递归左右两边继续取各自中点，作为每一个子树的根节点，

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res = []
        if not root:
            return res
        self.inOrder(root, res)
        if len(res) == 0:
            return 
        return self.constrTree(res, 0, len(res)-1)

    def constrTree(self, nums, l, r):
        if l > r:
            return 
        m = l + (r-l)/2
        root = TreeNode(nums[m])
        root.left = self.constrTree(nums, l, m - 1)
        root.right = self.constrTree(nums, m + 1, r)
        return root


    def inOrder(self, root, res):
        if not root:
            return 

        l = self.inOrder(root.left, res)
        res.append(root.val)
        r = self.inOrder(root.right, res)
        
