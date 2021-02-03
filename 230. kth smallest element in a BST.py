给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

解题思路：
BST中序遍历得到的数组必然是单调递增的，返回数组中第K-1个元素即可。

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = []
        self.inOrder(root)
        return self.res[k-1]
    
    def inOrder(self, root):
        if not root:
            return 
        self.inOrder(root.left)
        self.res.append(root.val)
        self.inOrder(root.right)
